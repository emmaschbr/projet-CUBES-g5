<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Required meta tags-->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="au theme template">
    <meta name="author" content="Hau Nguyen">
    <meta name="keywords" content="au theme template">

    <!-- Title Page-->
    <title>Projet CUBES - Station Météo - Groupe5</title>

    <!-- Fontfaces CSS-->
    <link href="vendor/font-awesome-4.7/css/font-awesome.min.css" rel="stylesheet" media="all">
    <link href="vendor/font-awesome-5/css/fontawesome-all.min.css" rel="stylesheet" media="all">

    <!-- Main CSS-->
    <link href="css/theme.css" rel="stylesheet" media="all">

    <script src="https://cdn.amcharts.com/lib/4/core.js"></script>
    <script src="https://cdn.amcharts.com/lib/4/charts.js"></script>
    <script src="https://cdn.amcharts.com/lib/4/themes/animated.js"></script>

    <!-- Graph -->
    <script>
    let chart;
    am4core.ready(function() {

    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end

    // Create chart instance
    var chart = am4core.create("chartdiv", am4charts.XYChart);

    // Export
    chart.exporting.menu = new am4core.ExportMenu();

    // Data for both series
    var data = <?php echo (file_get_contents("http://localhost:5000/mesures")); echo ";";?>

    /* Create axes humidité */
    var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
    categoryAxis.dataFields.category = "releve";
    categoryAxis.renderer.minGridDistance = 30;

    /* Create value axis */
    var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    valueAxis.numberFormatter = new am4core.NumberFormatter();
    valueAxis.numberFormatter.numberFormat = "#'g/m³'";

    /* Create value axis temperature*/
    var valueAxis2 = chart.yAxes.push(new am4charts.ValueAxis());
    valueAxis2.renderer.opposite = true;
    //valueAxis2.syncWithAxis = valueAxis;
    valueAxis2.tooltip.disabled = true;
    valueAxis2.numberFormatter = new am4core.NumberFormatter();
    valueAxis2.numberFormatter.numberFormat = "#'°C'"

    /* Create series */
    var columnSeries = chart.series.push(new am4charts.ColumnSeries());
    columnSeries.name = "humidite";
    columnSeries.dataFields.valueY = "humidite";
    columnSeries.dataFields.categoryX = "releve";
    columnSeries.fill = am4core.color("#fdd400");
    columnSeries.columns.template.tooltipText = "[#fff font-size: 15px]{name} le {categoryX}:\n[/][#fff font-size: 20px]{valueY}[/] [#fff]{additional}[/]"
    columnSeries.tooltip.label.textAlign = "middle";

    var lineSeries = chart.series.push(new am4charts.LineSeries());
    lineSeries.name = "temperature";
    lineSeries.dataFields.valueY = "temperature";
    lineSeries.yAxis = valueAxis2;
    lineSeries.dataFields.categoryX = "releve";

    lineSeries.stroke = am4core.color("#04A9F5");
    lineSeries.strokeWidth = 3;
    lineSeries.propertyFields.strokeDasharray = "lineDash";
    lineSeries.tooltip.label.textAlign = "middle";

    var bullet = lineSeries.bullets.push(new am4charts.Bullet());
    bullet.fill = am4core.color("#04A9F5"); // tooltips grab fill from parent by default
    bullet.tooltipText = "[#fff font-size: 15px]{name} le {categoryX}:\n[/][#fff font-size: 20px]{valueY}[/] [#fff]{additional}[/]"
    var circle = bullet.createChild(am4core.Circle);
    circle.radius = 4;
    circle.fill = am4core.color("#fff");
    circle.strokeWidth = 3;

    chart.data = data;

    }); // end am4core.ready()
    </script>

    <!-- Map -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css" integrity="sha512-Rksm5RenBEKSKFjgI3a41vrjkw4EVPlJ3+OiI65vTjIdo9brlAacEuKOiQ5OFh7cOI1bkDwLqdLw3Zg0cRJAAQ==" crossorigin="" />
    <style type="text/css">
        #map{ /* la carte DOIT avoir une hauteur sinon elle n'apparaît pas */
            height:400px;
        }
    </style>

</head>

<body class="animsition">
    <div class="page-wrapper">
        <!-- MENU SIDEBAR-->
        <aside class="menu-sidebar2">
            <div class="logo">
                <a href="#">
                    <img src="images/groupe5logo2.png" alt="" />
                </a>
            </div>
            <div class="menu-sidebar2__content js-scrollbar1">
                <div class="account2">
                    <div class="image img-cir img-120">
                        <img src="images/user_pic_a_clain" alt="Alexandre Clain" />
                    </div>
                    <h4 class="name">Alexandre Clain</h4>
                    <a href="#">Sign out</a>
                </div>
                <nav class="navbar-sidebar2">
                    <ul class="list-unstyled navbar__list">
                        <li class="active has-sub">
                            <a class="js-arrow" href="#">
                                <i class="fas fa-tachometer-alt"></i>Dashboard
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </aside>
        <!-- END MENU SIDEBAR-->

        <!-- PAGE CONTAINER-->
        <div class="page-container2">
            <!-- HEADER DESKTOP-->
            <header class="header-desktop2">
                <div class="section__content section__content--p30">
                    <div class="container-fluid">
                    </div>
                </div>
            </header>
            <!-- END HEADER DESKTOP-->

            <!-- BREADCRUMB-->
            <section class="au-breadcrumb m-t-75">
                <div class="section__content section__content--p30">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-md-12">
                                <div class="au-breadcrumb-content">
                                    <div class="au-breadcrumb-left">
                                        <span class="au-breadcrumb-span">Bonjour Alexandre Clain - </span>
                                        <span class="au-breadcrumb-span">La température actuelle est de
                                            <?php
                                                $jsonunformat = file_get_contents("http://localhost:5000/mesures");
                                                $jsonformat = (json_decode($jsonunformat, true));
                                                echo $jsonformat[0]['temperature'];
                                                ?>°C - </span>
                                        <ul class="list-unstyled list-inline au-breadcrumb__list">
                                            <li class="list-inline-item active">
                                                <p><?php echo date("d.m.Y"); ?></p>
                                            </li>
                                        </ul>
                                    </div>
                                    <button class="au-btn au-btn-icon au-btn--green">
                                      <ul class="share-buttons" data-source="simplesharingbuttons.com">
                                        <li><a href="https://www.facebook.com/sharer/sharer.php?u=https://www.google.com"
                                               title="Share on Facebook"
                                               target="_blank"
                                               onclick="window.open('https://www.facebook.com/sharer/sharer.php?u=https://www.google.com' + '&quote=' + encodeURIComponent(document.URL)); return false;"><img alt="Share on Facebook" src="images/simple_icons_black/Facebook.png" /></a>
                                        </li>
                                        <li><a href="https://twitter.com/intent/tweet?source=http%3A%2F%2Flocalhost%2FPROJCUBES%2FCoolAdmin-master%2F&text="
                                               target="_blank"
                                               title="Tweet"
                                               onclick="window.open('https://twitter.com/intent/tweet?text=' + encodeURIComponent(document.title) + ':%20'  + encodeURIComponent(document.URL)); return false;"><img alt="Tweet" src="images/simple_icons_black/Twitter.png" /></a>
                                        </li>
                                        <li><a href="mailto:?subject=&body=:http%3A%2F%2Flocalhost%2FPROJCUBES%2FCoolAdmin-master%2F&text="
                                               target="_blank"
                                               title="Send email"
                                               onclick="window.open('mailto:?subject=' + encodeURIComponent(document.title) + '&body=' +  encodeURIComponent(document.URL)); return false;"><img alt="Send email" src="images/simple_icons_black/Email.png" /></a>
                                        </li>
                                    </ul>
                                  </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!-- END BREADCRUMB-->

            <section>
                <div class="section__content section__content--p30">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-xl 12">
                                <!-- RECENT REPORT 2-->
                                <div class="recent-report2">
                                    <h3 class="title-3">Rapport des mesures météorologiques</h3>
                                    <div id="chartdiv"></div>
                                </div>
                                <!-- END RECENT REPORT 2             -->
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <section>
                <div class="section__content section__content--p30">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-xl-12">
                                <!-- MAP DATA-->
                                <div class="map-data m-b-40">
                                    <h3 class="title-3 m-b-30">
                                        <i class="zmdi zmdi-map"></i>map data</h3>
                                    <div class="map-wrap m-t-45 m-b-80">
                                        <div id="vmap" style="height: 284px;">
                                            <div id="map">
                                                <!-- Ici s'affichera la carte -->
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- END MAP DATA-->
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <section>
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="copyright">
                                <p>Copyright © 2021 Groupe5. All rights reserved. Template by Groupe5 CESI.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!-- END PAGE CONTAINER-->
        </div>

    </div>

    <!-- Jquery JS-->
    <script src="vendor/jquery-3.2.1.min.js"></script>
    <!-- Bootstrap JS-->
    <script src="vendor/bootstrap-4.1/popper.min.js"></script>
    <script src="vendor/bootstrap-4.1/bootstrap.min.js"></script>
    <!-- Vendor JS       -->
    <script src="vendor/slick/slick.min.js">
    </script>
    <script src="vendor/wow/wow.min.js"></script>
    <script src="vendor/animsition/animsition.min.js"></script>
    <script src="vendor/bootstrap-progressbar/bootstrap-progressbar.min.js">
    </script>
    <script src="vendor/counter-up/jquery.waypoints.min.js"></script>
    <script src="vendor/counter-up/jquery.counterup.min.js">
    </script>
    <script src="vendor/circle-progress/circle-progress.min.js"></script>
    <script src="vendor/perfect-scrollbar/perfect-scrollbar.js"></script>
    <script src="vendor/select2/select2.min.js">
    </script>
    <script src="vendor/vector-map/jquery.vmap.js"></script>
    <script src="vendor/vector-map/jquery.vmap.min.js"></script>
    <script src="vendor/vector-map/jquery.vmap.sampledata.js"></script>
    <script src="vendor/vector-map/jquery.vmap.world.js"></script>

    <script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js" integrity="sha512-/Nsx9X4HebavoBvEBuyp3I7od5tA0UzAxs+j83KgC8PU0kgB4XiK4Lfe4y4cgBtaRJQEIFCW+oC506aPT2L1zw==" crossorigin=""></script>
    <script type="text/javascript">
        // On initialise la latitude et la longitude de Paris (centre de la carte)
        var lat = 48.852969;
        var lon = 2.349903;
        var macarte = null;

        <?php
        $test = file_get_contents("http://localhost:5000/localisations");
        $test1 = json_decode($test, true);
        echo $test;
        ?>
        var villes = {
            <?php
            foreach($test1 as $key => $jsons)
                {
                    echo ( "\"".$test1[$key]['nom']."\": { \"lat\"  : ".$test1[$key]['latitude'].", \"lon\" : ".$test1[$key]['longitude']."},\n\t\t\t" );
                }
            ?>
        }
        // Fonction d'initialisation de la carte
        function initMap() {

            // Créer l'objet "macarte" et l'insèrer dans l'élément HTML qui a l'ID "map"
            macarte = L.map('map').setView([48.8566969, 2.3514616] /* point d'init de carte */ , 5 /* niveau de zoom */);
            // Leaflet ne récupère pas les cartes (tiles) sur un serveur par défaut. Nous devons lui préciser où nous
            // souhaitons les récupérer. Ici, openstreetmap.fr
            L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
                // Il est toujours bien de laisser le lien vers la source des données
                attribution: 'données © <a href="//osm.org/copyright">OpenStreetMap</a>/ODbL - rendu ' +
                    '<a href="//openstreetmap.fr">OSM France</a>',
                minZoom: 1,
                maxZoom: 20
            }).addTo(macarte);
            for (ville in villes) {
                var marker = L.marker([villes[ville].lat, villes[ville].lon]).addTo(macarte);
                // Nous ajoutons la popup. A noter que son contenu (ici la variable ville) peut être du HTML
                marker.bindPopup(ville)
            }
        }
        window.onload = function(){
            // Fonction d'initialisation qui s'exécute lorsque le DOM est chargé
            initMap();
        };
    </script>

    <!-- Main JS-->
    <script src="js/main.js"></script>

</body>

</html>
<!-- end document-->
