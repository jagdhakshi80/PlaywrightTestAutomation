# PlaywrightTestAutomation

docker compose run --rm playwright-tests

open reports/report.html



docker compose run --rm playwright-tests pytest tests/ -v

docker compose run --rm playwright-tests pytest tests/ -v --html=reports/report.html --self-contained-html

open reports/report.html


python3 -m compileall -q tests/

docker compose run --rm playwright-tests python -m compileall -q tests/

docker compose run --rm playwright-tests pytest tests/ -v --html=reports/report.html --self-contained-html --junitxml=test-results/junit.xml

open reports/report.html

**BUILD DOCKER IMAGES

cd /Users/arulmanii/Documents/Repo/AIApps/2026_Playright_test

docker compose down

docker compose build --no-cache

***START HEADED MODE


docker compose run --rm --service-ports playwright-tests


**LIVE EXECUTION

http://localhost:6080/vnc.html 


***

docker compose down
docker compose build

docker compose run --rm --service-ports playwright-tests

docker compose run --rm --service-ports playwright-tests pytest tests/ -v

**REPORTS


cd /Users/arulmanii/Documents/Repo/AIApps/2026_Playright_test

open reports/report.html

docker compose run --rm playwright-tests \
pytest tests/ -v \
--html=reports/report.html \
--self-contained-html \
--junitxml=test-results/junit.xml


open reports/report.html

docker compose run --rm --service-ports playwright-tests

docker compose build --no-cache


docker compose run --rm --service-ports playwright-tests

