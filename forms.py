from datetime import datetime
from flask_wtf import FlaskForm as Form
from choices import *
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL


class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired('start_time is required')], default=datetime.today()
    )


class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired('name is required')]
    )
    city = StringField(
        'city', validators=[DataRequired('city is required')]
    )
    state = SelectField(
        'state', validators=[DataRequired('state is required')],
        choices=state_choices
    )
    address = StringField(
        'address', validators=[DataRequired('address is required')]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired('genres is required'), AnyOf([x[1] for x in genre_choices], 'Invalid genre')],
        choices=genre_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL('facebook url is not valid')]
    )
    website_link = StringField(
        'website_link', validators=[URL('website link is not valid')]
    )

    seeking_talent = BooleanField('seeking_talent')

    seeking_description = StringField(
        'seeking_description'
    )


class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired('name is required')]
    )
    city = StringField(
        'city', validators=[DataRequired('city is required')]
    )
    state = SelectField(
        'state', validators=[DataRequired('state is required'), AnyOf([x[1] for x in state_choices], 'Invalid State')],
        choices=state_choices
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired('genres is required')],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL('facebook url is not valid')]
    )

    website_link = StringField(
        'website_link', validators=[URL('website link is not valid')]
    )

    seeking_venue = BooleanField('seeking_venue')

    seeking_description = StringField(
        'seeking_description'
    )
