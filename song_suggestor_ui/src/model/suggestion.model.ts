import { SongAnalysis } from "./song-analysis.model";

export class Suggestion {

    title: string;
    artist: string;
    lyrics?: string;

    analysis?: SongAnalysis;

    constructor(title: string, artist: string, lyrics?: string, analysis?: SongAnalysis) {
        this.title = title;
        this.artist = artist;
        this.lyrics = lyrics;
        this.analysis = analysis;
    }

}
