from mutagen.id3 import ID3, TIT2, TPE1, TALB, TPE2, TXXX, TRCK

def manage_tags(file_path):
    
    audio = ID3(file_path)
    
    #get tags
    title = audio.get('TIT2', [None])
    artist = audio.get('TPE1', [None])
    album = audio.get('TALB', [None])
    albumArtist = audio.get('TPE2', [None])
    artists = audio.getall('TXXX:ARTISTS')[0].text
    track_number = audio.get('TRCK', [None])
    
    print(f"Titolo: {title}")
    print(f"Artista: {artist}")
    print(f"Album: {album}")
    print(f"Album Artist: {albumArtist}")
    print(f"Artisti: {artists}")
    
    
    #edit tags
    if title is None or artist is None or artists is None:
        return

    # Split the list of artists
    artists_list = ', '.join(artists).split(', ') if artists else []
    
    principal_artist = artists[0]
    
    # Remove the main artist from the list of featured artists
    if principal_artist in artists_list:
        artists_list.remove(principal_artist)
        
    # Create a string with the list of featured artists
    feat_artists = ' & '.join(artists_list)

    # Check if feat artists are set, if not set it to the list of featured artists
    if f"(feat. {feat_artists})" not in title:
        new_title = f"{title} (feat. {feat_artists})"
        audio['TIT2'] = TIT2(encoding=3, text=new_title)
        print(f"Titolo aggiornato: {new_title}")
        # audio.save()
    
    # Check if artist is set, if not set it to the principal artist
    if artist != principal_artist:
        audio['TPE1'] = TPE1(encoding=3, text=principal_artist)
        print(f"Artista aggiornato: {principal_artist}")
        # audio.save()
        
    # Check if album is set, if not set it to the artist name    
    if albumArtist != principal_artist:
        audio['TPE2'] = TPE2(encoding=3, text=principal_artist)
        print(f"Album Artist aggiornato: {principal_artist}")
        # audio.save()
        
    # Check if track number is set, if not set it to 1
    if track_number is None:
        audio['TRCK'] = TRCK(encoding=3, text='1')
        print("Track number impostato a 1")
        # audio.save()
        
    
    

  
 
def print_tags(file_path):
    try:
        audio = ID3(file_path)
        for tag in audio.values():
            print(f"{tag.FrameID}: {tag.text}")

    except Exception as e:
        print(f"Errore nel caricamento del file: {e}")
        
        



if __name__ == "__main__":
    file_path = "/Users/davideresigotti/Desktop/PIOVE.mp3"
  
    # print_tags(file_path)
    manage_tags(file_path)
