import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SuggestionResultComponent } from './suggestion-result.component';

describe('SuggestionResultComponent', () => {
  let component: SuggestionResultComponent;
  let fixture: ComponentFixture<SuggestionResultComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SuggestionResultComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SuggestionResultComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
