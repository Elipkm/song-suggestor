import { Injectable } from "@angular/core";
import { Suggestion } from "../model/suggestion.model";
import { Observable, of } from "rxjs";
import { SuggestionResultDto } from "../model/suggestion-result-dto.model";
import { MOCK_ANALYSE, SongAnalysis } from "../model/song-analysis.model";
import { HttpClient } from "@angular/common/http";

@Injectable({providedIn: 'root'})
export class SuggestionService {

    constructor(private http: HttpClient){}

    URL = "http://localhost:5000/api/suggest"
    
    getSuggestions(inputLyrics: string): Observable<SuggestionResultDto> {
        console.log("get suggestions")
        return this.http.post<SuggestionResultDto>(this.URL, {inputLyrics});
        //return of(this.getMockSuggestions());
    }

    private getMockSuggestions(): SuggestionResultDto {
        return new SuggestionResultDto([
            new Suggestion("Money", "Pink Floyd", "", new SongAnalysis(MOCK_ANALYSE)),
            new Suggestion("Stairway to heaven", "Led Zeppelin","", new SongAnalysis(MOCK_ANALYSE)),
            new Suggestion("Uptown Funk", "Bruno Mars","", new SongAnalysis(MOCK_ANALYSE)),
            new Suggestion("Dancing Queen", "ABBA","", new SongAnalysis(MOCK_ANALYSE)),
            new Suggestion("Bohemian Rhapsody", "Queen","", new SongAnalysis(MOCK_ANALYSE))
        ], new SongAnalysis(MOCK_ANALYSE));
    }
}