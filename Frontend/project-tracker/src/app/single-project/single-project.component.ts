import { Component, OnInit } from '@angular/core';
import { HashLocationStrategy } from '@angular/common';
import { SingleProjectService } from '../services/single-project.service';
import { catchError,map } from 'rxjs/operators';
import { HttpClient,HttpHeaders,HttpErrorResponse,HttpRequest,HttpHandler} from '@angular/common/http';
import { Router, ActivatedRoute } from "@angular/router";

@Component({
  selector: 'app-single-project',
  templateUrl: './single-project.component.html',
  styleUrls: ['./single-project.component.css']
})

export class SingleProjectComponent implements OnInit {
  project: any;

  constructor(private SPService: SingleProjectService,  private router: Router, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.Project();
  }

  Project(){
    this.SPService.getProject('id').subscribe(project => {
      this.project = project;
      console.log(this.project)
    })
  }
}