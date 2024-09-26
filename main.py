from mutagen.id3 import ID3, TIT2, TPE1, TALB, TPE2, TXXX, TRCK
import re

def manage_tags(file_path):
    
    audio = ID3(file_path)
    
    #get tags
    title = audio.get('TIT2', [None])
    artist = audio.get('TPE1', [None])
    album = audio.get('TALB', [None])
    albumArtist = audio.get('TPE2', [None])
    artists = audio.getall('TXXX:ARTISTS')[0] if audio.getall('TXXX:ARTISTS') else None
    track_number = audio.get('TRCK', [None])
    
    # Get the first title to compare to album name to check if it's a single
    first_title = title[0] if title else None
    
    # Get the first artist to compare to artist
    first_artists = artists if artists else None
    
    
    print(f"Titolo: {title}")
    print(f"Artista: {artist}")
    print(f"Album: {album}")
    print(f"Album Artist: {albumArtist}")
    print(f"Artisti: {artists}")
    print()
    
    
    #edit tags
    
    if title is None or artist is None:
        print("no artist or title")
        return


    # Split the list of artists
    if artists is None:
        artists = artist
    artists_list = ', '.join(artists).split(', ')
        
    # Get the main artist
    principal_artist = artists[0]
    
    # Remove the main artist from the list of featured artists
    if principal_artist in artists_list:
        artists_list.remove(principal_artist)
        
    # Create a string with the list of featured artists
    feat_artists = ' & '.join(artists_list)
    
    
    
        
    
    # TITLE
    # Check if feat artists are set, if not set it to the list of featured artists
    title = title[0]
    if "feat" not in title:
        new_title = f"{title} (feat. {feat_artists})"
        print("feat not in title")
    elif "(feat." in title and title != f"{title} (feat. {feat_artists})":
        new_title = re.sub(r'\(feat\..*', f"(feat. {feat_artists})", title)
        print("(feat in title")
    elif "feat." in title:
        new_title = re.sub(r'\feat\..*', f"(feat. {feat_artists})", title)
        print("feat. in title")

    audio['TIT2'] = TIT2(encoding=3, text=new_title)
    print(f"Titolo aggiornato: {new_title}")
    
    #ARTIST
    # Check if artist is set, if not set it to the principal artist
    if artist != principal_artist:
        audio['TPE1'] = TPE1(encoding=3, text=principal_artist)
        print(f"Artista aggiornato: {principal_artist}")
        
    #ALBUM
    # Chek if the track is a single, if so set the album name to singles
    if first_title == album:
        audio['TALB'] = TALB(encoding=3, text='singles')
        print("Album impostato a singles")
        
    #TRACK NUMBER
    # Check if track number is set, if not set it to 1
    if track_number is None:
        audio['TRCK'] = TRCK(encoding=3, text='1')
        print("Track number impostato a 1")
    
    #ALBUM ARTIST
    # Check if album artist is set, if not set it to the artist name    
    if albumArtist != principal_artist:
        audio['TPE2'] = TPE2(encoding=3, text=principal_artist)
        print(f"Album Artist aggiornato: {principal_artist}")
        
    #ARTISTS
    # if artists is None 
    # add to the array of artists
    if first_artists is None:
        artists_list.insert(0, principal_artist)
        audio['TXXX:ARTISTS'] = TXXX(encoding=3, text=artists_list, desc='ARTISTS')
        print(f"Artisti aggiornati: {audio['TXXX:ARTISTS']}")
  
        
    audio.save()
    

  
 
def print_tags(file_path):
    try:
        audio = ID3(file_path)
        for tag in audio.values():
            print(f"{tag.FrameID}: {tag.text}")

    except Exception as e:
        print(f"Errore nel caricamento del file: {e}")
        
        



if __name__ == "__main__":
    file_path = '/Users/davideresigotti/Desktop/03 Emoji della traphouse.mp3'
  
    # print_tags(file_path)
    manage_tags(file_path)
