import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AcademComponent } from './academ.component';

describe('AcademComponent', () => {
  let component: AcademComponent;
  let fixture: ComponentFixture<AcademComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AcademComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AcademComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
