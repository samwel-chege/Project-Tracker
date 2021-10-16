import { Component, OnInit } from '@angular/core';
import { UserService } from '../_services/user.service';
import { HomeService } from '../services/home.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {
  projects: any;
  constructor(private HService: HomeService) { }

  ngOnInit(): void {
    this.AllProjects();
  }

  AllProjects() {
    this.HService.getprojects().subscribe(projects => {
      this.projects = projects;
      console.log(this.projects);
    })
  }

}
