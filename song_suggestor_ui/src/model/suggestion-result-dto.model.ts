import { SongAnalysis } from "./song-analysis.model";
import { Suggestion } from "./suggestion.model";

export class SuggestionResultDto {  
    suggestionList: Suggestion[];
    inputSongAnalysis: SongAnalysis;

    constructor(suggestionList: Suggestion[], inputSongAnalysis: SongAnalysis) {
        this.suggestionList = suggestionList;
        this.inputSongAnalysis = inputSongAnalysis;
    }
}