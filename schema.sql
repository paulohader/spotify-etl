CREATE TABLE charts (
    chart_id INT IDENTITY(1,1) PRIMARY KEY,
    chart VARCHAR(50)
);

----------------------------------------------

CREATE TABLE artists (
    artist_id INT IDENTITY(1,1) PRIMARY KEY,
    artist_name VARCHAR(255)
);

----------------------------------------------

CREATE TABLE regions (
    region_id INT IDENTITY(1,1) PRIMARY KEY,
    region_name VARCHAR(255)
);

----------------------------------------------

CREATE TABLE main (
    stream_id INT IDENTITY(1,1) PRIMARY KEY,
    title VARCHAR(255),
    rank INT,
    date DATE,
    artist_id INT,
    url VARCHAR(255),
    region_id INT,
    chart_id INT,
    trend VARCHAR(50),
    streams INT,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
    FOREIGN KEY (region_id) REFERENCES regions(region_id),
    FOREIGN KEY (chart_id) REFERENCES charts(chart_id)
);