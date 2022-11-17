import { ComponentFixture, TestBed } from '@angular/core/testing';
import { TablesDataComponent } from 'src/app/components/tables-data/tables-data.component';

import { UsersProfileComponent } from './users-profile.component';

describe('UsersProfileComponent', () => {
  let component: UsersProfileComponent;
  let fixture: ComponentFixture<UsersProfileComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UsersProfileComponent, TablesDataComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UsersProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
