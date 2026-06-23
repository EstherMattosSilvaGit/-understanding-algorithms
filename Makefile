.PHONY: test clean help

help:
	@echo Comandos disponiveis:
	@echo   make test    - Rodar todos os testes
	@echo   make clean   - Limpar cache Python (__pycache__ e .pytest_cache)
	@echo   make help    - Mostrar esta mensagem

test:
	python -m unittest discover --pattern="*Tests.py" -v

clean:
	@echo Limpando caches...
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
	@for /d /r . %%d in (.pytest_cache) do @if exist "%%d" rmdir /s /q "%%d"
	@echo Cache limpado!

.DEFAULT_GOAL := help
