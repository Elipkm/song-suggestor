import { Component, Input } from '@angular/core';
import { SongAnalysis } from '../../model/song-analysis.model';
import { Suggestion } from '../../model/suggestion.model';
import { AccordionModule } from 'primeng/accordion';

@Component({
  selector: 'app-suggestion-explanation',
  imports: [AccordionModule],
  templateUrl: './suggestion-explanation.component.html',
  styleUrl: './suggestion-explanation.component.css'
})
export class SuggestionExplanationComponent {

  @Input() inputSongAnalysis?: SongAnalysis;
  @Input() suggestions: Suggestion[] = [];


}
