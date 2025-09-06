Downloader de Playlists do YouTube para MP3 (yt-dlp)
================================================================

Baixe toda uma playlist do YouTube em MP3 (192 kbps), pulando automaticamente os vídeos indisponíveis/privados, e organizando os arquivos com numeração e o nome da playlist.

Usa a biblioteca yt-dlp + FFmpeg.

----------------------------------------------------------------
1) O QUE ESTE SCRIPT FAZ
----------------------------------------------------------------
- Baixa o melhor áudio disponível de cada item da playlist
- Converte para MP3 192 kbps (via FFmpeg)
- Ignora vídeos problemáticos e continua o download
- Salva em: music/<Título da Playlist>/<índice> - <título>.mp3

Exemplo de estrutura:
music/
  └── Minha Playlist
      ├── 001 - Primeira faixa.mp3
      ├── 002 - Segunda faixa.mp3
      └── 003 - ...

----------------------------------------------------------------
2) PRÉ-REQUISITOS
----------------------------------------------------------------
- Python 3.8 ou superior
- FFmpeg instalado e no PATH
  - Windows (Chocolatey): choco install ffmpeg
  - Windows (Scoop):      scoop install ffmpeg
  - macOS (Homebrew):     brew install ffmpeg
  - Debian/Ubuntu:        sudo apt-get install ffmpeg
- yt-dlp atualizado:
  python -m pip install -U yt-dlp

----------------------------------------------------------------
3) COMO USAR
----------------------------------------------------------------
a) Clone este repositório:
   git clone https://github.com/<seu-usuario>/<seu-repo>.git
   cd <seu-repo>

b) (Opcional) Crie um ambiente virtual:
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate

c) Instale dependências:
   python -m pip install -U yt-dlp

d) Edite o arquivo principal (por exemplo, main.py) e ajuste a URL da playlist se quiser.
   O script já possui um exemplo no final do arquivo.

e) Execute:
   python main.py

Por padrão, os arquivos serão salvos em music/.
Para mudar a pasta de saída, altere o parâmetro pasta_saida ao chamar baixar_playlist.

----------------------------------------------------------------
4) CÓDIGO PRINCIPAL (REFERÊNCIA DE USO)
----------------------------------------------------------------
# Exemplo de chamada:
baixar_playlist("https://youtube.com/playlist?list=...")              # salva em "music"
baixar_playlist("https://youtube.com/playlist?list=...", "meus_mp3")  # salva em "meus_mp3"

O script inclui:
- ignoreerrors: continua mesmo se algum vídeo falhar
- retries e fragment_retries: novas tentativas em falhas temporárias
- skip_unavailable_fragments: evita abortar por fragmentos ausentes
- pós-processador FFmpeg para MP3 192 kbps

----------------------------------------------------------------
5) PERSONALIZAÇÕES ÚTEIS
----------------------------------------------------------------
a) Usar cookies do seu navegador (para vídeos com restrição):
   No dicionário 'opcoes', adicione:
   opcoes["cookiesfrombrowser"] = ("chrome",)  # ou ("edge",), ("firefox",), ("opera",)

b) Definir caminho do FFmpeg (se não estiver no PATH):
   opcoes["ffmpeg_location"] = r"C:\caminho\para\ffmpeg\bin"

c) Mudar a qualidade do MP3 (128, 192, 256, 320):
   "postprocessors": [{
     "key": "FFmpegExtractAudio",
     "preferredcodec": "mp3",
     "preferredquality": "256"
   }]

----------------------------------------------------------------
6) SOLUÇÃO DE PROBLEMAS
----------------------------------------------------------------
- "Video unavailable / This video is not available"
  O item pode estar removido, privado ou bloqueado por região. O script irá pular e seguir.

- "ffmpeg not found"
  Instale o FFmpeg e/ou ajuste o PATH ou 'ffmpeg_location'.

- Erros intermitentes de rede
  O script já tenta novamente (retries). Se persistir, tente em outro horário ou rede.

- Nada foi baixado
  Confirme se a playlist é pública ou use cookies do navegador (cookiesfrombrowser).

- Atualize o yt-dlp
  python -m pip install -U yt-dlp

----------------------------------------------------------------
7) CONTRIBUINDO
----------------------------------------------------------------
Sugestões e melhorias são bem-vindas! Abra uma Issue ou PR (ex.: opção de baixar intervalo, formatos alternativos, etc.).

----------------------------------------------------------------
8) AVISO LEGAL
----------------------------------------------------------------
Baixar conteúdo pode violar os Termos de Serviço da plataforma e/ou direitos autorais.
Use apenas para conteúdos de sua autoria, domínio público ou com permissão do detentor dos direitos.

----------------------------------------------------------------
9) LICENÇA
----------------------------------------------------------------
Recomenda-se incluir uma licença (ex.: MIT).

Observação: Para o GitHub renderizar automaticamente como página inicial do repositório, renomeie este arquivo para README.md.
