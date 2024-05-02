#!/usr/bin/env bash

# --------------------------------------------------------------------------------------------------
#
# Update translation files
#
# Supported locales on FreeCAD <2024-01-20, FreeCADGui.supportedLocales(), total=40>:
# 	{'English': 'en', 'Afrikaans': 'af', 'Arabic': 'ar', 'Basque': 'eu', 'Belarusian': 'be',
# 	'Bulgarian': 'bg', 'Catalan': 'ca', 'Chinese Simplified': 'zh-CN',
# 	'Chinese Traditional': 'zh-TW', 'Croatian': 'hr', 'Czech': 'cs', 'Dutch': 'nl',
# 	'Filipino': 'fil', 'Finnish': 'fi', 'French': 'fr', 'Galician': 'gl', 'Georgian': 'ka',
# 	'German': 'de', 'Greek': 'el', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it',
# 	'Japanese': 'ja', 'Kabyle': 'kab', 'Korean': 'ko', 'Lithuanian': 'lt', 'Norwegian': 'no',
# 	'Polish': 'pl', 'Portuguese': 'pt-PT', 'Portuguese, Brazilian': 'pt-BR', 'Romanian': 'ro',
# 	'Russian': 'ru', 'Serbian': 'sr', 'Serbian, Latin': 'sr-CS', 'Slovak': 'sk',
# 	'Slovenian': 'sl', 'Spanish': 'es-ES', 'Spanish, Argentina': 'es-AR', 'Swedish': 'sv-SE',
# 	'Turkish': 'tr', 'Ukrainian': 'uk', 'Valencian': 'val-ES', 'Vietnamese': 'vi'}
#
# NOTE: WORKFLOW
# 0. Install Qt tools
# 	Debian-based (e.g., Ubuntu): $ sudo apt-get install qttools5-dev-tools pyqt6-dev-tools
# 	Fedora-based: $ sudo dnf install qt6-linguist qt6-devel
# 	Arch-based: $ sudo pacman -S qt6-tools python-pyqt6
# 1. Make the script executable
# 	$ chmod +x update_translation.sh
# 2. Execute the script passing the locale code as first parameter
# 	The script has to be executed within the `resources/translations` directory
# 	Only update the files you're translating!
# 	$ ./update_translation.sh es-ES
# 3. Do the translation via Qt Linguist and use `File>Release`
# 4. If releasing with the script execute the script passing the locale code as first parameter
# 	and use '-r' flag next
# 	$ ./update_translation.sh es-ES -r
#
# NOTE: If some of QT binaries have different names in your distro (e.g Fedora has -qt5 suffix)
# you can change it names using LUPDATE,LCONVERT,LRELEASE,PYLUPDATE env variables
#
# --------------------------------------------------------------------------------------------------

lupdate_command="${LUPDATE:-lupdate}"
lconvert_command="${LCONVERT:-lconvert}"
lrelease_command="${LRELEASE:-lrelease}"
pylupdate_command="${PYLUPDATE:-pylupdate5}"

supported_locales=(
	"en" "af" "ar" "eu" "be" "bg" "ca" "zh-CN" "zh-TW" "hr"
	"cs" "nl" "fil" "fi" "fr" "gl" "ka" "de" "el" "hu"
	"id" "it" "ja" "kab" "ko" "lt" "no" "pl" "pt-PT" "pt-BR"
	"ro" "ru" "sr" "es-ES" "es-AR" "sv-SE" "tr" "uk" "val-ES" "vi"
)

is_locale_supported() {
	local locale="$1"
	for supported_locale in "${supported_locales[@]}"; do
		if [[ "${supported_locale,,}" == "$locale" ]]; then
			return 0
		fi
	done
	return 1
}

get_strings() {
	# Get translatable strings from ../*.py Python files
	$pylupdate_command -verbose ../*.py -ts pyfiles.ts
}

delete_files() {
	# Delete files that are no longer needed
	rm pyfiles.ts
	rm -f _${WB}.ts
}

add_new_locale() {
	echo -e "\033[1;33m\n\t<<< Creating '${WB}_${LOCALE}.ts' file >>>\n\033[m"
	get_strings
	# Join strings from Qt Designer and Python files
	# Add generic file
	$lconvert_command -i pyfiles.ts -o ${WB}.ts
	# Add specified locale file
	$lconvert_command -source-language en -target-language $LOCALE \
		-i pyfiles.ts -o ${WB}_${LOCALE}.ts
}

update_locale() {
	echo -e "\033[1;32m\n\t<<< Updating '${WB}_${LOCALE}.ts' file >>>\n\033[m"
	get_strings
	# Join strings from Qt Designer and Python files
	$lconvert_command -i pyfiles.ts -o _${WB}.ts
	# Join newly created file with older file (-no-obsolete)
	# Update generic file
	$lconvert_command -i _${WB}.ts ${WB}.ts -o ${WB}.ts
	# Update specified locale file
	$lconvert_command -source-language en -target-language $LOCALE \
		-i _${WB}.ts ${WB}_${LOCALE}.ts -o ${WB}_${LOCALE}.ts
}

release_translation() {
	# Release translation (creation of *.qm file from *.ts file)
	$lrelease_command ${WB}_${LOCALE}.ts
}

# Main function ------------------------------------------------------------------------------------

WB="woodwoking"
# Convert to lowercase
LOCALE="${1,,}"

if is_locale_supported "$LOCALE"; then
	if [ "$2" == "-r" ]; then
		release_translation
	else
		if [ ! -f "${WB}_${LOCALE}.ts" ]; then
			add_new_locale
		else
			update_locale
		fi
		delete_files
	fi
else
	echo "Verify your language code. Case sensitive."
	echo "If it's correct ask a maintainer to add support for your language on FreeCAD."
fi
