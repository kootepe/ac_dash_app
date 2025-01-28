# Instructions

General instructions for using the app.

## Initiating data

At the top go to ```Go to Settings``` > ```Data initiation``` > ```Initiate from file```.

#### Upload gas measurement

Here you can upload gas measurements from gas analyzers. From the dropdown
select your instrument and give it some short short but descriptive name, eg.
```AC fen LICOR```, this name will be displayed around the app to see which
instrument you are processing data from. 

Also specify the serial of the instrument. This should be the actual serial of
the instrument, eg. for LI-7810 the format is TG10-XXXXX. Currently the timestamp, serial
and instrument model are used to prevent uploading duplicate rows into the
database. So if you don't know the actual serial, at least make it unique.

Then you can upload files by drag and drop or clicking and selecting files. The
app accepts .dat/.DAT .data/.DATA, .csv and .zip extensions. I'd recommend using
zips when uploading locally but there's also an API for uploading
programmatically.

### Upload cycles

The dropdown currently does nothing, the app accepts the log files for from the
AC app (The newer ones with 4 rows for each cycle) and a precalculated version
with this format:
```
chamber_id,start_time,close_offset,open_offset,end_offset
1,2024-01-01 00:00:00,300,600,900
2,2024-01-01 00:15:00,300,600,900
3,2024-01-01 00:30:00,300,600,900
4,2024-01-01 00:45:00,300,600,900
```
Where the offsets are the seconds from start_time.

### Upload meteo data

Select new source from the dropdown and give it a descriptive name, it will be
used to select which meteo data will be used for flux calculation.
format:
```
datetime,air_temperature,air_pressure
1,2024-01-01 00:30:00,-10.0,994.5
```

### Upload volume data

Chamber height should be in meters.

format:
```
datetime,chamber_id,chamber_height
2024-01-01 12:00:00,1,0.94
2024-01-08 12:00:00,2,0.75
```

### Initiate fluxes

Select your instrument and meteo source from the dropdowns and then specify a
range to calculate fluxes from.

Accepts ISO8601 dates eg. YYYY-MM-DD, YYYY-MM-DD HH:MM:SS etc.

