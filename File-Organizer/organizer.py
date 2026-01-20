import os
import shutil
from pathlib import Path

EXTENSOES = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Vídeos": [".mp4", ".mkv", ".avi"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Compactados": [".zip", ".rar", ".7z"]
}

def organizar(pasta):
    pasta = Path(pasta)

    if not pasta.exists():
        print("❌ Pasta não encontrada")
        return

    for arquivo in pasta.iterdir():
        if arquivo.is_file():
            movido = False
            for categoria, extensoes in EXTENSOES.items():
                if arquivo.suffix.lower() in extensoes:
                    destino = pasta / categoria
                    destino.mkdir(exist_ok=True)
                    shutil.move(str(arquivo), destino / arquivo.name)
                    movido = True
                    break

            if not movido:
                destino = pasta / "Outros"
                destino.mkdir(exist_ok=True)
                shutil.move(str(arquivo), destino / arquivo.name)

    print("✅ Arquivos organizados com sucesso!")

if __name__ == "__main__":
    caminho = input("Digite o caminho da pasta: ")
    organizar(caminho)
