// set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 30, left: 60},
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

//Read the data
d3.csv("Cleaned_Data.csv", function(data) {

  // Add X axis
  var x = d3.scaleLinear()
    .domain([0, 35.0])
    .range([ 0, width ]);
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));
    svg.append("text")
    .attr("class", "x label")
    .attr("text-anchor", "end")
    .attr("x", (width/2) + 40)
    .attr("y", height + 28)
    .text("Number of Labs");
    

  // Add Y axis
  var y = d3.scaleLinear()
    .domain([0, 720])
    .range([ height, 0]);
  svg.append("g")
    .call(d3.axisLeft(y));
    svg.append("text")
    .attr("class", "y label")
    .attr("text-anchor", "end")
    .attr("y", -40)
    .attr("dy", ".75em")
    .attr("transform", "rotate(-90)")
    .text("University Rank");
    

  // Add dots
  svg.append('g')
    .selectAll("dot")
    .data(data)
    .enter()
    .append("circle")
      .attr("cx", function (d) { return x(d.no_of_labs); } )
      .attr("cy", function (d) { return y(d.university_rank); } )
      .attr("r", 1.5)
      .style("fill", "#69b3a2")

})