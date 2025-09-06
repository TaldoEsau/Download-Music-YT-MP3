
import os
import yt_dlp

def baixar_playlist(playlist_url: str, pasta_saida: str = "music"):
    os.makedirs(pasta_saida, exist_ok=True)

    opcoes = {
        "format": "bestaudio/best",

        "outtmpl": {
            "default": f"{pasta_saida}/%(playlist_title|Unknown Playlist)s/%(playlist_index)03d - %(title)s.%(ext)s"
        },

        "ignoreerrors": "only_download",

        "retries": 10,
        "fragment_retries": 10,
        "extractor_retries": 3,

        "skip_unavailable_fragments": True,

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],


        "noprogress": False,
        "quiet": False,
        "no_warnings": False,

    }


    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([playlist_url])


if __name__ == "__main__":
    url = "link da playlist YT"
    print("Iniciando download da playlist...")
    baixar_playlist(url)
    print("✅ Download concluído! (Itens problemáticos foram ignorados)")
