@echo off
echo.
echo.
echo Starting manual test for garble.py...
python garble.py ./test/manual/inbox/pii.csv ./test/manual/schema ./test/manual/deidentification_secret.txt
echo.
echo Done.  
echo.
echo.

