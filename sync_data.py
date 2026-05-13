#!/usr/bin/env python3
"""
Sincroniza dados do Google Sheets para JSON com encoding correto.
Executa regularmente para manter o dashboard atualizado.
"""

import requests
import csv
import json
import sys
from datetime import datetime
from io import StringIO
from pathlib import Path

SHEET_ID = "1vOlvmsj65CKsqRqj1EftY4zTLO3IIWA8yhsrAch1-sk"
GID_MSGS = "754433413"
GID_CLI = "907718646"

def fetch_csv(gid):
    """Fetch CSV from Google Sheets com encoding correto."""
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={gid}"
    try:
        resp = requests.get(url, timeout=10)
        resp.encoding = 'utf-8'  # Forçar UTF-8
        return resp.text
    except Exception as e:
        print(f"[ERROR] Erro ao buscar GID {gid}: {e}", file=sys.stderr)
        return None

def fix_encoding_errors(text):
    """Corrige caracteres que foram interpretados errado do Latin-1 como UTF-8.

    Google Sheets retorna UTF-8 decodificado como Latin-1, então "á" vira "Ã¡".
    Para corrigir: codificar como Latin-1, depois decodificar como UTF-8.
    """
    try:
        # Tenta a estratégia de re-codificação
        fixed = text.encode('latin-1').decode('utf-8')
        return fixed
    except (UnicodeDecodeError, UnicodeEncodeError):
        # Se falhar, retorna o original
        return text

def parse_csv(raw_csv):
    """Parse CSV mantendo encoding UTF-8."""
    if not raw_csv:
        return []

    # Usar StringIO para manter encoding
    f = StringIO(raw_csv)
    reader = csv.DictReader(f)
    rows = []
    for row in reader:
        # Garantir que todos os valores estão UTF-8 e corrigir encoding
        cleaned = {}
        for k, v in row.items():
            val = str(v or '').strip()
            val = fix_encoding_errors(val)
            cleaned[k] = val
        rows.append(cleaned)
    return rows

def sync_data():
    """Sincronizar dados e salvar em JSON."""
    print(f"[SYNC] Sincronizando dados... {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Buscar dados
    print("[FETCH] Buscando mensagens...")
    csv_msgs = fetch_csv(GID_MSGS)
    if not csv_msgs:
        print("[ERROR] Falha ao buscar mensagens", file=sys.stderr)
        return False

    print("[FETCH] Buscando clientes...")
    csv_cli = fetch_csv(GID_CLI)
    if not csv_cli:
        print("[ERROR] Falha ao buscar clientes", file=sys.stderr)
        return False

    # Parsear
    print("[PROCESS] Processando dados...")
    msgs = parse_csv(csv_msgs)
    clientes = parse_csv(csv_cli)

    if not msgs or not clientes:
        print("[ERROR] Nenhum dado foi parseado", file=sys.stderr)
        return False

    # Montar estrutura
    data = {
        "timestamp": datetime.now().isoformat(),
        "sheet_id": SHEET_ID,
        "messages": msgs,
        "customers": clientes,
        "stats": {
            "message_count": len(msgs),
            "customer_count": len(clientes)
        }
    }

    # Salvar JSON com UTF-8
    output_file = Path(__file__).parent / "data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[OK] Dados sincronizados com sucesso!")
    print(f"[STATS] Mensagens: {len(msgs)}")
    print(f"[STATS] Clientes: {len(clientes)}")
    print(f"[STATS] Salvo em: {output_file}")
    return True

if __name__ == '__main__':
    try:
        success = sync_data()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"[ERROR] Erro geral: {e}", file=sys.stderr)
        sys.exit(1)
