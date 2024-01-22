---
layout: page
title: Simplified Table
permalink: /simplified-table/
---
<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>CSV to HTML Table</title>
    <meta name="author" content="Derek Eder">
    <meta content="Display any CSV file as a searchable, filterable, pretty HTML table">

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
        crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/dataTables.bootstrap4.min.css">
</head>

<div id="table-container"></div>

<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.2.1/js/bootstrap.bundle.min.js"></script>
<script src="../assets/js/jquery.csv.min.js"></script>
<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.10.19/js/dataTables.bootstrap4.min.js"></script>
<script src="../assets/js/csv_to_html_table.js"></script>
<script>
	function format_image(link) {
		if (link){
			position = link.search("id=");
			hash = link.substring(position+3,link.length);
			finalLink = "https://drive.google.com/thumbnail?id=" + hash;
			return "<a href='https://www.google.com'> <img src='" + finalLink + "'> </a>";
		}
		else return "";
	}
    function format_email(string) {
    	newString = string.replace("@", "\n_at_");
    	newString = newString.replace(".", "_dot_");
    	return newString
    }

    CsvToHtmlTable.init({
        csv_path: "../assets/nimeTestSimplified.csv",
        element: "table-container",
        allow_download: true,
        csv_options: {
            separator: ",",
            delimiter: '"'
        },
        datatables_options: {
            paging: false,
            scrollY: true,
            fixedHeader: false,
            lengthChange: true,
            autoWidth: false

        },
        custom_formatting: [
        	[1, format_image],
        	[3, format_email]
        ]
    });
</script>


