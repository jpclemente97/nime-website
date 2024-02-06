---
layout: page
title: Exchange
permalink: /exchange/
---

To date, hundreds of NIMEs have been built, presented at conferences, and used in live performances. Even after many years, some of these NIME may still exist, eventually maintained in working conditions. Making these NIMEs available to others can be immensely beneficial for our community. These can be used in other studies, compared with improved versions of the same conceptual design, or further developed by other researchers. Artists can engage with such unique musical devices, master skills, and feature these in their performances and compositions. Such activities can further inform the research of the original author, and promote new artistic or academic collaborations.

If you ***own a NIME*** that you would like to make available to other artists or researchers, fill up this [form](https://docs.google.com/forms/d/e/1FAIpQLSfcWRfPuj4KBqp3WplTrtnX636scaNdMWUZLBeddRCKWAErMw/viewform?usp=sf_link). The form includes a comprehensive set of questions about the owner, status, and current location of the device. It also asks who can access the device, where they can access it, for how long they can access it, and whether the device can be loaned or even donated.
A few days after submitting the form, your NIME will be listed on the table below. If you wish to remove your submission, [contact us](mailto:stefano.fasciani@imv.uio.no?subject=NIMExchange).

If you wish to ***use or borrow a NIME***, check out the devices listed in the table below, as well as the full details listed in the [extended version of the table](/exchange-full-table/). Then get in touch with the owner and enter in a dialogue to find an agreement.
Volunteers from the NIME community can facilitate the dialogue between Owner and User/Borrower. However the NIME committee and volunteers will not take any responsibility for the final agreement, which is solely between Owner and User/Borrower. Also, the committee and volunteers are not responsible for problems that may arise from such activities and they do not offer mediation. Below, there is a set of [recommendations](#recommendations) that both Owner and interested User/Borrower should consider before exchanging a NIME.  

<br/><br/> 

<head>
    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
        crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/dataTables.bootstrap4.min.css">
</head>

<div id="table-container"></div>

<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.2.1/js/bootstrap.bundle.min.js"></script>
<script src="../assets/exchange/jquery.csv.min.js"></script>
<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.10.19/js/dataTables.bootstrap4.min.js"></script>
<script src="../assets/exchange/csv-to-html-table.js"></script>
<script>
	function format_image(link) {
		if (link){
			position = link.search("id=");
			hash = link.substring(position+3,link.length);
			ThumbLink = "https://drive.google.com/thumbnail?id=" + hash;
            DirectLink = "https://drive.google.com/uc?id=" + hash;
            return "<a href='" + DirectLink + "'> <img src='" + ThumbLink + "'> </a>";
		}
		else return "";
	}

    CsvToHtmlTable.init({
        csv_path: "../assets/exchange/exchange-table-small.csv",
        element: "table-container",
        allow_download: false,
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
        	[2, format_image]
        ]
    });
</script>

<br/><br/> 

[**View extended version of table**](/exchange-full-table/)

<br/><br/> 

#### Recommendations

* Users or Borrowers should submit a written request or expression of interest to the Owner, specifying the scope, objective, and timeframe.

* Owners are highly encouraged to document their NIME, for example using [Documentation and Replicability in the NIME Community](https://www.nime.org/proc/nime21_4/index.html) or [Open Source DMIs: Towards a replication certification for online shared projects of digital musical instruments](https://link.springer.com/chapter/10.1007/978-3-030-60114-0_5).

* The Owner and User/Borrower should enter into a dialogue to:

    * Clarify mutual expectations, especially if establishing a research collaboration. Remember, most NIMEs are research probes or prototypes, not commercial products.

    * Assess risks, clarify responsibilities and costs, especially if items are damaged or lost.

    * Consider insurance if shipping the NIME and note possible customs fees or issues.

    * Discuss potential copyright or licensing issues.

    * Address any ethical issues or conflicts of interest.

    * Explore the best and most sustainable options for exchanging the NIME. For example, a physical exchange can occur during a conference, or geographically close colleagues, when traveling, may assist.

    * If the User/Borrower is part of a study and data is being collected, provide information and obtain written participation consent.

    * All these points should be briefly documented in a signed agreement by both parties.

* Owners might find it useful to keep a 'history' of Users/Borrowers. For example, this could support future borrowers in troubleshooting the NIME. It might also be helpful to make anonymized borrowing data available for future meta studies or musicological inquiries.
