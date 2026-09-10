#!/bin/bash

# Проверить скомпилирован ли мод
rpyc_files=$(find src -type f -name "*.rpyc")
if [ -z "$rpyc_files" ]; then
	echo "Предупреждение: Файлы rpyc не найдены. Вы скомпилировали мод?"
	exit
fi

# Создать директорию файлов сборки
rm -rf build
mkdir -p build/scenario_slavyana

# Скопировать файлы rpyc
find src -type f -name "*.rpyc" -exec cp {} build/scenario_slavyana/ \;

# Скопировать ресурсы
cp -r res build/scenario_slavyana/

# Сгенерировать readme
cat <<EOF > build/README.txt
КАК УСТАНОВИТЬ:

	Переместите директорию (папку) scenario_slavyana в директорию (папку) game внутри игры.

	Например, если у вас игра находится по пути C:\\\steam\steamapps\common\Everlasting Summer
	То у вас должно получиться следущее:

		C:\\\steam\steamapps\common\Everlasting Summer\game\scenario_slavyana
EOF

# Вывести напоминание
echo -e "\nВсе готово! Файлы находятся в директории build\n"
cat build/README.txt