import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SuggestionExplanationComponent } from './suggestion-explanation.component';

describe('SuggestionExplanationComponent', () => {
  let component: SuggestionExplanationComponent;
  let fixture: ComponentFixture<SuggestionExplanationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SuggestionExplanationComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SuggestionExplanationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
