echo cd %cd% > runs.bat
echo call conda activate my_python_env >> runs.bat
echo call scrapy crawl stockbots >> runs.bat
call schtasks /create /tn "scrapy_demo" /tr %cd%\runs.bat /sc minute /mo 10