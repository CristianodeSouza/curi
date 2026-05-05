# CURI — Projeto de Dados via Google Sheets

## Planilha Principal
- **URL:** https://docs.google.com/spreadsheets/d/1vOlvmsj65CKsqRqj1EftY4zTLO3IIWA8yhsrAch1-sk/edit?gid=907718646#gid=907718646
- **ID da Planilha:** `1vOlvmsj65CKsqRqj1EftY4zTLO3IIWA8yhsrAch1-sk`
- **ID da Aba:** `907718646`

## MCP Configurado
Este projeto usa o MCP `@modelcontextprotocol/server-gdrive` para acesso direto ao Google Drive/Sheets.

## Autenticação
As credenciais OAuth ficam em `.credentials/gdrive_credentials.json`.
Execute `npm run auth` para autenticar pela primeira vez.

## Estrutura
```
curi/
├── .claude/settings.json     # Configuração MCP
├── .credentials/             # Credenciais OAuth (não commitar)
├── src/                      # Código fonte
└── CLAUDE.md                 # Este arquivo
```
