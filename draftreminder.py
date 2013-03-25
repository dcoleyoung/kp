from fantext import *

def reminder_email_pick(this_league, owner, available_players, pick, results, host):
    message = mail.EmailMessage(sender="Fantasizr <noreply@fantasizr.appspotmail.com>",subject="Fantasizr " + this_league.league_name + " Reminder: Draft Pick #" + str(pick))
    message.to = owner
    message.body = "It's still your turn to make a pick.  Click a player name to make your pick\n"
    message.html = """
	<table width="650" align="center" style="font-size: 14px;" cellpadding="0" cellspacing="0">
	        <tr id="header">
	            <td width="10" bgcolor="#ffffff" rowspan="2"></td>
	            <td height="52" bgcolor="#dae7e1" align="center">
	                <table width="95%%"><tr>
	                    <td align="left">
	                        <img src="http://%s/static/images/email_logo.jpg"/>
	                    </td>
	                </tr></table>
	            </td>
	            <td width="10" bgcolor="#ffffff" rowspan="2"> </td>
	        </tr>

	        <tr id="content">
	            <td bgcolor="#edf4f1" align="center">
	                <table width="95%%" cellpadding="30">
	                    <tr>
	                        <td align="left">
	                            <font face="Helvetica Neue, Helvetica, Arial, sans-serif">
	Just a friendly reminder, It's your turn to make the next pick.  Select the player you want to pick by clicking a name below. <br>
	""" % host
    for player in available_players:
      full_player = db.get(player)
      message.body += full_player.player_name + ": http://%s/draftplayer?league=" % host + str(this_league.key().id()) + "&player=" + str(full_player.key().id()) + "&owner=" + owner + "&current_pick=" + str(pick) + "\n"
      if full_player.link != "http://dummy.com":
        message.html += "<a href=http://%s/draftplayer?league=" % host + str(this_league.key().id()) + "&player=" + str(full_player.key().id()) + "&owner=" + owner + "&current_pick=" + str(pick) + ">"+ full_player.player_name + "</a>" +  \
      "&nbsp;<a href="+ full_player.link +">Bio</a><br>"
      else:
	    message.html += "<a href=http://%s/draftplayer?league=" % host + str(this_league.key().id()) + "&player=" + str(full_player.key().id()) + "&owner=" + owner + "&current_pick=" + str(pick) + ">"+ full_player.player_name + "</a><br>"
    message.body += "\n Current Draft Results:\n"
    message.html += "<br> Current Draft Results:<br>"
    for entry in results:
      message.body += entry + "\n"
      message.html += entry + "<br>"
    message.html += """<br/><br/> 
		                            </font>
		                        </td>
		                    </tr>
		<tr><td><a href="http://%s">Fantasizr.com</a> - Create your own fantasy league out of ANYTHING.</td></tr>
		                </table>
		            </td>
		        </tr>

		        <tr id="bottomshadow">
		            <td height="10" width="10"   bgcolor="#ffffff"></td>
		            <td height="10" bgcolor="#ffffff"> </td>
		            <td height="10" width="10" bgcolor="#ffffff"> </td>
		        </tr>

		    <tr id="copyright">
		        <td></td>
		        <td align="right">
		            <span style="font-family: Helvetica Neue, Helvetica, Arial, sans-serif; font-size: 11px; color: #888;">&copy;&nbsp;2012&nbsp;Fantasizr</span>
		        </td>
		        <td></td>
		    </tr>

		    </table>
	""" % host
    message.send()

draftboard_query = DraftBoard.all()
draftboard_query.filter("draft_status =", False)
draft_boards = draftboard_query.fetch(100) #template leagues
for this_db in draft_boards:
  if this_db.key().id():
    owner = this_db.owners_pickorder[((this_db.current_pick) % len(this_db.owners_pickorder)) - 1] #determine current owner to make pick
    reminder_email_pick(this_db.league,owner, this_db.available_players, this_db.current_pick, this_db.draft_history, self.request.host)

