@echo off
set /p message="Enter migration name: "
cd migrations
alembic revision -m "%message%"
