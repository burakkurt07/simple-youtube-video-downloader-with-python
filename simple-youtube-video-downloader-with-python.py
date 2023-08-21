import pytube

def display_progress(stream, chunk, file_handle, remaining_bytes):
    if remaining_bytes % 100 == 0:
        progress = int(file_handle.tell() * 100 / (file_handle.tell() + remaining_bytes))
        print(progress, '%')

def choose_stream(streams):
    print('Choose video quality:')
    for i, stream in enumerate(streams):
        print(f'{i}. Resolution: {stream.resolution}, Format: {stream.subtype}')

    choice = int(input())
    return streams[choice]

def main():
    input_link = input('Enter YouTube video link: ')
    yt = pytube.YouTube(input_link)

    yt.register_on_progress_callback(display_progress)
    
    video_streams = yt.streams.filter(subtype='mp4', progressive=True).all()
    selected_stream = choose_stream(video_streams)
    
    output_path = input('Enter download path (leave empty for current directory): ')
    
    if output_path:
        selected_stream.download(output_path)
    else:
        selected_stream.download()
    
    print('Download completed!')

if __name__ == "__main__":
    main()
