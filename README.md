# NBA_Name_Chains

## General Overview 
There has long been a fascination amongst NBA fans to create NBA Name Chains. A name chain is a chain of names connected by a first name last name similarity. For example, Bob Taylor - Taylor James - James Will - Will O'brien would be a name chain. In this chain, the last name of a player matches the first name of the next player. 

There have been several attempts at creating the longest name in chains in the NBA. Most of these attempts represent the NBA Player database using a graph with each player being a node and edges between players existing if a name chain link is possible. 

My attempt instead chooses to use a relational database structure and creates links in name chains by self joining a table of NBA player names. In addition, I generate simple metrics in order to determine how useful a player name is in generating long name chains. 

## Technology Used
I use python to handle the data processing, the table self join, and the metric generation. Tableau is used for a basic data visualization. 

## Metrics generated 
- Name Points: a score for how important a name is in generating long name chains. If a name is part of many long name chains, the name receives more points. Fewer points are allotted to names that generate fewer, shorter name chains. More points the better. 
- Name Percentile: assigns a percentile to the name points that a name earns 
- Name Replaceability Points: Marks the replaceability of a name, if a name is more generic, it will receive more points (a higher score). If a name is less generic and less replaceable, it will receive fewer points. 
- Replaceability Percentile: assigns a percentile to the replaceability points that a name earns

## Visualization 
A public Tableau workbook can be found at the link below: 
https://public.tableau.com/profile/adi.srikanth#!/vizhome/NbaNames/Sheet1
