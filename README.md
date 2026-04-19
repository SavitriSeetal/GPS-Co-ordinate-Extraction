# Title : GPS Coordinate Extraction
In multi-site monitoring operations geospatial data collection often involves capturing hundreds of field photos. The legacy workflow required manual extraction of GPS coordinates from image properties and hand-typing them into master field sheets. This created a systemic bottleneck:

Time-Intensive: Manual entry took hours per site visit.

Error-Prone: High risk of transcription errors (typos in coordinates).

Delayed Delivery: Quality Control (QC) could only begin after manual data entry was finalized.

Therefore, I designed a custom Python-based ETL pipeline that programmatically interfaces with image EXIF metadata.
The Key Technical Achievements are as follows :
1) Automated Extraction: Developed a batch-processing engine using exifread to pull latitude/longitude tags from raw .jpg files.

2) Coordinate Transformation: Built a robust conversion algorithm to translate Degrees/Minutes/Seconds (DMS) into Decimal Degrees (DD) for immediate GIS compatibility.

3) Seamless Integration: Utilized Pandas to structure data into validated Excel and CSV formats, ready for database ingestion.
