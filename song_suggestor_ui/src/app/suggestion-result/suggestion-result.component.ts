import { Component, Input } from '@angular/core';
import { Suggestion } from '../../model/suggestion.model';
import { ButtonModule } from 'primeng/button';
import { AccordionModule } from 'primeng/accordion';

@Component({
  selector: 'app-suggestion-result',
  imports: [ButtonModule, AccordionModule],
  templateUrl: './suggestion-result.component.html',
  styleUrl: './suggestion-result.component.css'
})
export class SuggestionResultComponent {

  @Input() suggestions: Suggestion[] = [];


  searchForSong(suggestion: Suggestion) {
    console.log("search for song: " + suggestion.title + " by " + suggestion.artist);
    // open new tab and search for song
    let searchUrl = "https://www.youtube.com/results?search_query=" + suggestion.title + " " + suggestion.artist;
    window.open(searchUrl, '_blank');
  }

}
