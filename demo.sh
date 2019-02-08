#!/usr/bin/env bash
APIURL=http://ec2-54-186-185-206.us-west-2.compute.amazonaws.com/api/v1
clear
echo =========================
echo * peAk Backend API Demo *
echo =========================
read
echo List resorts [Enter]:
echo
echo http $APIURL/resort
read
echo
http $APIURL/resort
echo
echo Get a resort [Enter]:
echo
echo http $APIURL/resort/1
read
http $APIURL/resort/1
echo
######## Register a user
echo ===============
echo Register a user
echo ===============
echo
echo http POST $APIURL/register username=testuser99 password=s0mep@ssw0rd!
read
http POST $APIURL/register username=testuser99 password=s0mep@ssw0rd! email=test@user99.com
echo
######## Log in a user
echo =============
echo Log in a user
echo =============
echo
echo http POST $APIURL/login username=testuser99 password=s0mep@ssw0rd!
read
http POST $APIURL/login username=testuser99 password=s0mep@ssw0rd!
echo
######## View a team
echo ===========
echo View a team
echo ===========
echo
echo http GET $APIURL/team/1
read
http GET $APIURL/team/1
echo

echo Done.
