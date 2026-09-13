#!/bin/bash

# Проверить скомпилирован ли мод
rpyc_files=$(find src -type f -name "*.rpyc")
if [ -z "$rpyc_files" ]; then
	echo "Предупреждение: Файлы rpyc не найдены. Вы скомпилировали мод?"
	exit
fi

# Создать директорию файлов сборки
rm -rf build
mkdir -p build/content/scenario_slavyana

# Скопировать файлы rpyc
find src -type f -name "*.rpyc" -exec cp {} build/content/scenario_slavyana/ \;

# Скопировать ресурсы
cp -r res build/content/scenario_slavyana/

# Запросить описание изменений
read -p "Что изменилось?: " changenote

curr_path=$(pwd)

# Сгенерировать vdf файл для steam workshop
cat <<EOF > build/workshopitem.vdf
"workshopitem"
{
	"appid"	"331470"
	"publishedfileid"	"2304057650"
	"contentfolder"	"${curr_path}/build/content"
	"changenote"	"${changenote}"
}
EOF

# Сгенерировать readme для архивов
cat <<EOF > build/content/README.txt
КАК УСТАНОВИТЬ:

	Распакуйте директорию (папку) scenario_slavyana в game внутри игры.

	Например, если у вас игра находится по пути C:\\\steam\steamapps\common\Everlasting Summer
	То у вас должно получиться следущее:

		C:\\\steam\steamapps\common\Everlasting Summer\game\scenario_slavyana
EOF

# Архивируем
cd build/content
if command -v tar &> /dev/null; then
	tar -zcf ../scenario_slavyana.tar.gz scenario_slavyana README.txt
fi
if command -v zip &> /dev/null; then
	zip -r ../scenario_slavyana.zip scenario_slavyana README.txt
fi
rm README.txt

# Вывести напоминание
echo -e "\nВсе готово! Собранные архивы находятся в директории build\n"
echo "Напоминание по обновилению через steamcmd:"
echo "1) Авторизация: login <steam_login>"
echo "2) Залить мод: workshop_build_item ${curr_path}/build/workshopitem.vdf"