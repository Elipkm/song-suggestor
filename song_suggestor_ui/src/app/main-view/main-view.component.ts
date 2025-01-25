import { Component } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { TextareaModule } from 'primeng/textarea';
import { SuggestionResultComponent } from "../suggestion-result/suggestion-result.component";
import { FormsModule } from '@angular/forms';
import { SuggestionService } from '../../service/suggestion.service';
import { Suggestion } from '../../model/suggestion.model';
import { SongAnalysis } from '../../model/song-analysis.model';
import { SuggestionResultDto } from '../../model/suggestion-result-dto.model';
import { SuggestionExplanationComponent } from "../suggestion-explanation/suggestion-explanation.component";
import { ProgressSpinnerModule } from 'primeng/progressspinner';
import { ToastModule } from 'primeng/toast';
import { MessageService } from 'primeng/api';

@Component({
  selector: 'app-main-view',
  imports: [ButtonModule, TextareaModule, SuggestionResultComponent, 
    FormsModule, SuggestionExplanationComponent, ProgressSpinnerModule, ToastModule],
  templateUrl: './main-view.component.html',
  styleUrl: './main-view.component.css'
})
export class MainViewComponent {

  showExplanation: boolean = false;
  loading: boolean = false;

  inputLyrics: string = "";
  suggestions?: Suggestion[] = undefined;
  inputLyricsAnalysis?: SongAnalysis = undefined;

  private readonly suggestionService: SuggestionService;

  constructor(suggestionService: SuggestionService, private messageService: MessageService) {
    this.suggestionService = suggestionService;
  }

  suggestSongs() {
    this.loading = true;
    this.messageService.add({ severity: 'info', summary: 'Search has started', detail: 'Looking for similar songs - this may take up to one minute', life: 15000 });

    this.suggestionService.getSuggestions(this.inputLyrics)
      .subscribe((result: SuggestionResultDto) => {
        this.loading = false;
        this.suggestions = result.suggestionList;
        this.inputLyricsAnalysis = result.inputSongAnalysis;
      });
  }

  explain() {
    this.showExplanation = true;
  }
  hideExplanation() {
    this.showExplanation = false;
  }
  clear() {
    this.suggestions = undefined;
    this.showExplanation = false;
    this.inputLyrics = "";
  }
}
