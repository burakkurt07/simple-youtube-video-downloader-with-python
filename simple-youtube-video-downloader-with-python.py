import os
from yt_dlp import YoutubeDL
from youtubesearchpython import VideosSearch

def display_progress(d):
    if d['status'] == 'finished':
        print('İndirme tamamlandı!')

def choose_download_path():
    output_path = input('İndirme dizinini girin (boş bırakılırsa mevcut dizine indirilir): ')
    if output_path and not os.path.exists(output_path):
        os.makedirs(output_path)
    return output_path

def choose_video_name(video_title):
    return input(f'İndirilen video için özel bir ad girin (boş bırakılırsa otomatik ad: {video_title}): ') or video_title

def choose_resolution(video_streams):
    print('Video çözünürlüğünü seçin:')
    for i, stream in enumerate(video_streams):
        resolution = stream.get("resolution", "Bilinmiyor")
        format_note = stream.get("format_note", "Bilinmiyor")
        ext = stream.get("ext", "Bilinmiyor")
        print(f'{i}. Format Notu: {format_note}, Çözünürlük: {resolution}, Format: {ext}')

    while True:
        choice = input()
        if choice.isdigit() and 0 <= int(choice) < len(video_streams):
            return video_streams[int(choice)]
        else:
            print('Geçersiz giriş. Lütfen geçerli bir seçenek numarası girin.')

def download_video_by_link(video_link):
    try:
        ydl_opts = {
            'progress_hooks': [display_progress],
            'outtmpl': os.path.join(choose_download_path(), '%(title)s.%(ext)s'),
            'format': choose_resolution,
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_link, download=True)
            video_title = info_dict.get('title', 'Video')
            video_name = choose_video_name(video_title)
            print(f'{video_title} başarıyla indirildi!')
    except Exception as e:
        print(f'Hata oluştu: {str(e)}')

def search_and_download():
    query = input('YouTube videosunu arayın: ')
    try:
        videos_search = VideosSearch(query, limit=5)
        results = videos_search.result()
        print('Bulunan videolar:')
        for i, result in enumerate(results['result']):
            print(f'{i + 1}. {result["title"]}')

        choice = int(input('İndirmek istediğiniz video numarasını seçin: '))
        selected_video = results['result'][choice - 1]

        video_link = selected_video['link']
        download_video_by_link(video_link)

    except Exception as e:
        print(f'Hata: {str(e)}')

def list_downloaded_videos():
    download_path = choose_download_path()
    if not download_path:
        download_path = os.getcwd()

    print('İndirilen videolar:')
    for file in os.listdir(download_path):
        if file.endswith((".mp4", ".webm")):
            print(file)

def delete_downloaded_video():
    download_path = choose_download_path()
    if not download_path:
        download_path = os.getcwd()

    list_downloaded_videos()

    video_name = input('Silmek istediğiniz video dosyasının adını girin (uzantı olmadan): ')
    file_path = os.path.join(download_path, video_name + '.mp4')

    try:
        os.remove(file_path)
        print('Video silindi!')
    except FileNotFoundError:
        print('Belirtilen dosya bulunamadı.')

def main():
    while True:
        print('\n1. YouTube Video İndirme\n2. YouTube Video Ara ve İndir\n3. İndirilen Videoları Listele\n4. İndirilen Video Sil\n5. Çıkış')
        choice = input('Hangi işlemi yapmak istersiniz? ')

        if choice == '1':
            input_link = input('YouTube video bağlantısını girin: ')
            download_video_by_link(input_link)
        elif choice == '2':
            search_and_download()
        elif choice == '3':
            list_downloaded_videos()
        elif choice == '4':
            delete_downloaded_video()
        elif choice == '5':
            break
        else:
            print('Geçersiz seçenek, lütfen tekrar deneyin.')

if __name__ == "__main__":
    main()
