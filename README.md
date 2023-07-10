This program reads an audio stream from a microphone and tries
to interpret anything it hears as a phrase in a context-free
language with English words.

It's based on Mozilla Deepspeech: https://github.com/mozilla/DeepSpeech

To set it up:
```
    python3 -m venv --system-site-packages --symlinks env
    . env/bin/activate
    pip install -r requirements.txt
```

Possibly install libboost-timer1.67.0 and libboost-program-options1.67.0 and libboost-date-time1.67.0?

To run:
```
    ./startup
```

To change the context-free language it detects:
```
    cd context_free_grammar
    (edit the rules in *.gram, possibly adding more files)
    cd .. 
    ./generate_language_model
```
This last thing uses binaries that were compiled for Raspberry Pi, so if you want to run the generator on anything else, you'd have to compile new binaries and put them in cfrais/generator and cfrais/generator/bins.
See https://deepspeech.readthedocs.io/en/v0.9.3/Scorer.html

Change the RATE and DEVICE at the top of cfrais/chat.py to
match your microphone. If you don't know them, you can figure
them out with list_audio_input_devices.

The native sample rate of the VAD and model are 16000, so
if the sample rate isn't 16000 then it will resample using
libsamplerate.

Here are some examples of .gram files:

ice_cream_requests.gram
```
ice_cream_requests I WANT icecream
ice_cream_requests I WANT icecream IN cone_type

icecream flavour
icecream A SCOOP OF flavour
icecream TWO SCOOPS OF flavour
icecream A SCOOP OF flavour AND icecream

cone_type A WAFFLE CONE
cone_type A SUGAR CONE
cone_type MY STICKY HANDS

flavour VANILLA
flavour CHOCOLATE
flavour STRAWBERRY
flavour AMARETTO
```

Example sentences generated by this gram file:
```
I WANT TWO SCOOPS OF VANILLA IN A SUGAR CONE
I WANT A SCOOP OF STRAWBERRY AND VANILLA IN A WAFFLE CONE
I WANT A SCOOP OF VANILLA AND A SCOOP OF STRAWBERRY AND A SCOOP OF VANILLA
I WANT TWO SCOOPS OF AMARETTO IN A SUGAR CONE
I WANT TWO SCOOPS OF VANILLA IN A SUGAR CONE
I WANT TWO SCOOPS OF AMARETTO
I WANT AMARETTO
I WANT A SCOOP OF STRAWBERRY AND A SCOOP OF AMARETTO AND A SCOOP OF AMARETTO
I WANT TWO SCOOPS OF AMARETTO
```

You can also weight possibilities.

no_but_rarely_absolutely_not_and_never_yes.gram
```
no_but_rarely_absolutely_not_and_never_yes*12 NO
no_but_rarely_absolutely_not_and_never_yes*1 ABSOLUTELY NOT
no_but_rarely_absolutely_not_and_never_yes*0 YES
```

Example sentences generated by this gram file:
```
ABSOLUTELY NOT
NO
NO
NO
NO
NO
NO
NO
NO
ABSOLUTELY NOT
ABSOLUTELY NOT
```
