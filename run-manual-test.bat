@echo off
echo.
echo.
echo Starting manual test for garble.py...
@echo on
python garble.py ./test/manual/inbox/pii.csv ./test/manual/schema ./test/manual/deidentification_secret.txt
@echo off
echo.
echo Done.  
echo.
echo.

