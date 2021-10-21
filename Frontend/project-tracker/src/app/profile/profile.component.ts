import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../services/profile.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})

export class ProfileComponent implements OnInit {
  students: any;
  constructor(private PfService: ProfileService) { }

  ngOnInit(): void {
    this.AllProfiles();
  }

  AllProfiles() {
    this.PfService.getProfiles().subscribe(students => {
      this.students = students;
      console.log(this.students);
    })
  }

}
