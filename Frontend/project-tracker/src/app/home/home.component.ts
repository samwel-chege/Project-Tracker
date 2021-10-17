import { Component, OnInit } from '@angular/core';
import { UserService } from '../_services/user.service';
import { HomeService } from '../services/home.service';
import { ProjectService } from '../services/project.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {
  students: any;
  constructor(private HService: HomeService,) { }

  ngOnInit(): void {
    this.AllStudents();
  }

  AllStudents() {
    this.HService.getprofiles().subscribe(students => {
      this.students = students;
      console.log(this.students);
    })
  }

}
