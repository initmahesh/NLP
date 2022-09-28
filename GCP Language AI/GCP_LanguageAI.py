from html import entities
import re
from urllib import response
from google.cloud import language_v1

client = language_v1.LanguageServiceClient()

text_content = "@105836 LiveChat is online at the moment - _https://t.co/SY94VtU8Kq_ (https://t.co/SY94VtU8Kq) or contact 03331 031 031 option 1, 4, 3 (Leave a message) to request a call back \n \
@VirginTrains see attached error message. I've tried leaving a voicemail several times in the past week _https://t.co/NxVZjlYx1k_ (https://t.co/NxVZjlYx1k)"

document = language_v1.Document(content=text_content, type_=language_v1.Document.Type.PLAIN_TEXT)
# Available values: NONE, UTF8, UTF16, UTF32
encoding_type = language_v1.EncodingType.UTF8

response = client.analyze_entities(request={"document": document,"encoding_type":encoding_type})
# Loopthrough entities returned
print(response)
 # Loop through entitites returned from the API
for entity in response.entities:
    print(u"Representative name for the entity: {}".format(entity.name))

    # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
    print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))

    # Get the salience score associated with the entity in the [0, 1.0] range
    print(u"Salience score: {}".format(entity.salience))

    # Loop over the metadata associated with entity. For many known entities,
    # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
    # Some entity types may have additional metadata, e.g. ADDRESS entities
    # may have metadata for the address street_name, postal_code, et al.
    for metadata_name, metadata_value in entity.metadata.items():
        print(u"{}: {}".format(metadata_name, metadata_value))

    # Loop over the mentions of this entity in the input document.
    # The API currently supports proper noun mentions.
    for mention in entity.mentions:
        print(u"Mention text: {}".format(mention.text.content))

        # Get the mention type, e.g. PROPER for proper noun
        print(
            u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name)
        )

# Get the language of the text, which will be the same as
# the language specified in the request or, if not specified,
# the automatically-detected language.
print(u"Language of the text: {}".format(response.language))