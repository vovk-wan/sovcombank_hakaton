import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnaliticsComponent } from './analitics.component';

describe('AnaliticsComponent', () => {
  let component: AnaliticsComponent;
  let fixture: ComponentFixture<AnaliticsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AnaliticsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AnaliticsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
