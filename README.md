Creating powerful API's with Django 2.1, Django Rest Framework 3 and deploying on Heroku

creating a full project ( Customer Base ) with all database relationships, image upload and full control on what is happening behind the scenes.

Introduction

Preparing the environment

Creating the base of the application ( Customer base app )

Setup of the Django Rest Framework

Exposing an API for the Customer Endpoint

Consuming this API with Google Chrome and Postman

Creating the Endpoint for the all entities

Personalizing the get_queryset method to provide a list of Customers with filters

Override of the behaviour for the defaults HTTP verbs (Get, Post, Put, Patch, Delete )

Creating custom actions

Using query strings

Filtering querysets with DjangoFilter backend

Enabling API search

Custom lookup field

Improving the API security with Tokens

Custom permissions per token

Nested relationships

OneToOne

ForeignKey

ManyToMany

Types of Serializers

Nested serializers

Function fields

Types of ViewSets

Enabling Pagination on your API

Deploy on Heroku and updating versions of the application after deploy on Heroku
