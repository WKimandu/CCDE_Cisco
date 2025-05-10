Detecting language using up to the first 30 seconds. Use `--language` to specify the language
Detected language: English
[00:06.360 --> 00:11.020]  Hello everybody. Thanks for stopping by and listening to me talking about network design.
[00:11.620 --> 00:15.860]  My name is Mark Holm. I am the exam program manager for the CCD certification here at
[00:15.860 --> 00:22.360]  Learning and Certifications. So I talk network design all the time. That's what I do and that's
[00:22.360 --> 00:29.580]  how I make a living in my professional career at the moment. I make sure that if you go take
[00:29.580 --> 00:34.140]  the CCD exam, it's my job to make sure we test you the right way. But I'm not going to talk so
[00:34.140 --> 00:39.880]  much about the DE today. I'm going to talk much more about some of the stuff you need to know to
[00:39.880 --> 00:46.480]  be able to be a network designer. Because at the end of the day, network design is not just making
[00:46.480 --> 00:52.280]  some drawings in Visio or other drawing programs. This is about knowing the requirements, knowing
[00:52.280 --> 00:58.500]  your customer, knowing your organization to make sure they have or get what they need.
[00:59.920 --> 01:04.200]  So it's not just about technical knowledge. You need other things as well. So that's what I'm going
[01:04.200 --> 01:09.160]  to cover today. I'm going to give you an example that's going to look very simple, but it's going
[01:09.160 --> 01:16.760]  to have two very different outcomes depending on the requirements. So quickly, there is a
[01:16.760 --> 01:20.820]  Webex space for this. So after the session, if you registered, you should have been added to Room.
[01:21.300 --> 01:25.780]  If not, let us know. Otherwise, feel free to ask me questions afterwards if you have
[01:25.780 --> 01:28.220]  any follow-up questions or anything I've been saying today.
[01:31.400 --> 01:35.620]  So let's have a look at some of the required skills that you need.
[01:38.220 --> 01:45.860]  Because network design is not an exact science. You need to have technical knowledge and you need
[01:45.860 --> 01:52.100]  to have experience, right? Because without the experience, it will be harder for you to design
[01:53.000 --> 01:59.140]  well-functioning networks that are built to the purpose they are supposed to do.
[02:00.380 --> 02:03.800]  And then you need to understand the goals of what you are trying to do.
[02:04.100 --> 02:09.640]  So if you're working on a project, you need to understand why this project, what are the goals,
[02:10.120 --> 02:13.820]  what do you want to achieve, your customer or your organization, what are you trying to get
[02:13.820 --> 02:19.460]  to? Don't just blindly assume, oh, this is just a network. It won't be. There's going to be some
[02:19.460 --> 02:24.120]  requirements. There's going to be some business behind it that needs this to make sure they are
[02:24.120 --> 02:27.300]  fully able to utilize this network afterwards.
[02:29.580 --> 02:36.980]  And we see this every day. Network designs that are bad, they cause problems every day.
[02:38.040 --> 02:45.200]  So essentially, you spend a lot of time and money fixing those problems. Those money would have been
[02:45.200 --> 02:51.760]  much better spent making a proper design at the beginning of the project. But the thing here,
[02:52.460 --> 02:58.560]  and this is bullet number four here, is very important. There is no one size fits all. That
[02:58.560 --> 02:59.560]  doesn't exist. There is no one size fits all. There is no one size fits all. There is no one size fits all.  
[02:59.560 --> 03:04.820]  So when we talk about Cisco validated designs, they are very good. They are validated,
[03:05.000 --> 03:10.680]  of course, hence their name. But at the end of the day, they should be seen as a starting point.
[03:10.760 --> 03:16.900]  You need to trust and verify. Make sure it actually fits. Because there might be or likely
[03:16.900 --> 03:24.180]  will be a requirement somewhere in this information you get from your customer that says, we can't use       
[03:24.180 --> 03:28.580]  the solution as it is. We need to make some adjustments. And there's always going to be
[03:28.580 --> 03:29.220]  some tradeoffs somewhere.
[03:30.220 --> 03:37.000]  You can't build the coolest network ever built because the customer probably can't afford it.
[03:37.740 --> 03:45.120]  You need to make sure that you find a balance between features and what's actually needed.
[03:45.280 --> 03:50.020]  Don't just throw in a lot of features because somebody has to pay for it at the end of the day.
[03:50.600 --> 03:59.300]  And money, it always wins. Every time. No matter what you do, if there's no money to buy what you're
[03:59.300 --> 04:05.460]  suggesting, you won't win. It's going to be shut down. It's not going to be valid design for this
[04:05.460 --> 04:11.300]  game. So this is why you need not a master's degree, but you need a business understanding
[04:11.860 --> 04:17.180]  to be able to do proper network design and be a true expert in that field.
[04:21.180 --> 04:28.100]  So you need to be able to analyze and understand what you're working with, what you're working in,
[04:28.100 --> 04:32.600]  and who you're working for. If you don't have that understanding,
[04:32.920 --> 04:36.340]  chances are you will be making wrong decisions somewhere along the path
[04:36.340 --> 04:41.900]  and will fail to meet the requirements that you've been asked or tasked to do.
[04:43.900 --> 04:49.820]  So you need to make sure that whatever you do, it supports whatever goals and strategy are set for
[04:49.820 --> 04:54.840]  that business. Again, if you fail, they won't call you next time they need a design project.
[04:55.060 --> 04:57.560]  You need to make sure that whatever you do,
[04:58.100 --> 05:03.020]  is aligned with the strategy. So you need to ask questions. You need to make sure you understand
[05:03.020 --> 05:11.120]  this. Don't assume it. Verify it by asking. And then you need to, of course, meet all the
[05:11.120 --> 05:15.540]  requirements, but there's also going to be some constraints. It might be, oh, we can't use new
[05:15.540 --> 05:22.040]  technologies. We can't use, hopefully nobody says that today, but we can't use VXLAN. We will only
[05:22.040 --> 05:27.980]  use traditional VLANs. Okay? It might happen. But there might be constraints that you need
[05:27.980 --> 05:32.360]  to add to that will completely take away everything that you have learned recently here at
[05:32.360 --> 05:36.680]  Cisco Live. So this is a new, cool technology. This is what you should all be doing. But if a
[05:36.680 --> 05:42.080]  customer says, we don't want that, then you have to meet that requirement by not doing it.
[05:43.720 --> 05:47.840]  So again, it ties into that you know who you're working for. So if you're working on a new project,
[05:48.500 --> 05:53.020]  spend a little time researching the company name, researching what they do,
[05:53.180 --> 05:57.620]  what kind of company are you working with? Because if you do that, you might have a better
[05:57.980 --> 06:02.380]  understanding and a good starting point in succeeding and understanding what they're doing.
[06:05.680 --> 06:12.420]  You need, and we talk about this, I say business requirements. You also need to have deep,
[06:12.560 --> 06:18.640]  solid technical understanding of the features, the protocols, all the technologies. You need to
[06:18.640 --> 06:22.960]  have good knowledge of them. Because you need to know what kind of problems they can solve
[06:22.960 --> 06:27.000]  and how they can solve them. And you only have that by having a deep technical knowledge. You can
[06:27.000 --> 06:32.120]  just, oh, I think VLAN will be good here. You need to know why VLAN will be good. Because you need
[06:32.120 --> 06:38.400]  to ask them why questions. So if you talk about the CCIE, which is much more about implementation,
[06:38.820 --> 06:44.460]  so this is more how you do it. When you do a design, you have to ask why.
[06:46.600 --> 06:51.080]  Because you don't implement, you typically in a way, you don't implement as a network designer.
[06:51.300 --> 06:55.120]  You design the network and you hand it off to somebody else to actually do the implementation.
[06:55.860 --> 06:56.660]  You don't
[06:57.000 --> 07:02.160]  do everything yourself unless you're a very small organization where you might have both caps on.
[07:04.340 --> 07:09.340]  But most importantly, you have to size it right. Don't gold plate it. Again,
[07:09.440 --> 07:13.620]  it ties back to the requirements. If they don't have a requirement to do feature set,
[07:14.680 --> 07:19.900]  then don't put it there because it will be over plating and it will be a waste of time and
[07:19.900 --> 07:26.700]  resources to build in a feature they will never use or don't even want. And then lastly, this is
[07:27.000 --> 07:32.080]  where the business stuff come in. You need to be comfortable working with topics like CapEx, OpEx,
[07:32.840 --> 07:39.200]  TCO, total cost of ownership, return on investment. Because you need to understand, again, the money
[07:40.260 --> 07:46.220]  is king, not technology. So you need to be able to work with these numbers and figure out what's
[07:46.220 --> 07:50.380]  going to cost long, what's going to be OpEx, what's going to be CapEx. And you need to
[07:50.380 --> 07:55.900]  understand this could be cost of operating and owning this network. So not only the acquiring the
[07:55.900 --> 08:01.200]  hardware and requiring the, you know, the hours to implement it, you also need to operate it
[08:01.200 --> 08:05.740]  until the day you have to refresh everything. So remember, everything is cyclical. It all goes back.
[08:05.900 --> 08:10.440]  You design then you run it and at some point you're gonna go back and make a new design
[08:10.440 --> 08:16.800]  because things change and this is also what a designer does. Understand that there is always
[08:16.800 --> 08:24.020]  gonna be changes. One of the most important things you need to do is… Listen.
[08:25.340 --> 08:25.880]  Figuring out When you're doing something you'rewarting –and that's not a PRO – when you're
[08:25.880 --> 08:29.060]  set in meetings with your customer you have to listen to what they are saying
[08:29.680 --> 08:36.200]  and also what they're not saying because it's hardly ever going to happen to you
[08:36.200 --> 08:40.000]  that a customer is going to say exactly we want this and we want it like that
[08:40.820 --> 08:45.580]  they don't know it's your job so what they are saying and then what they're
[08:45.580 --> 08:49.800]  not saying listen to what's between blinds because they might not say
[08:49.800 --> 08:54.200]  directly so you need to be able to catch oh this is what you really want you're
[08:54.200 --> 08:59.020]  saying you wanting this but in reality you want something over here but often
[08:59.020 --> 09:04.360]  these people that you're talking to as a network signer might be CTOs or CFOs
[09:04.360 --> 09:09.520]  they might not know all the technical slides you need to be able to speak
[09:09.520 --> 09:13.600]  business language and understand that they are going to express something in
[09:13.600 --> 09:18.600]  what we need for our business and then you have to listen to them a figure out
[09:18.600 --> 09:22.960]  and translate that into the design at the end of the day so you're going to
[09:22.960 --> 09:23.820]  talk to a bunch of
[09:23.820 --> 09:23.980]  people
[09:23.980 --> 09:28.040]  relevant people, not only CTOs and things like that,
[09:28.100 --> 09:29.300]  but you're also going to talk to network engineers.
[09:29.500 --> 09:31.080]  You're going to talk to them, okay, so what do you need?
[09:31.220 --> 09:34.420]  What are your pain problems today?
[09:34.520 --> 09:36.060]  What do you struggle with today?
[09:36.500 --> 09:39.220]  And how can you, what are your skill sets?
[09:39.480 --> 09:40.800]  Because another thing you have to consider,
[09:40.920 --> 09:42.400]  if you're bringing brand new technology,
[09:42.660 --> 09:43.600]  there's also going to be training.
[09:44.620 --> 09:46.260]  If you don't have the necessary skills
[09:46.820 --> 09:48.260]  in the organization to run the network,
[09:48.400 --> 09:51.220]  again, it's not relevant, it's going to be useless
[09:51.220 --> 09:52.260]  at the end of the day.
[09:52.260 --> 09:54.960]  So if you get to a customer that doesn't have
[09:54.960 --> 09:58.200]  a budget for training or time for training, you lose.
[09:59.600 --> 10:02.060]  Because if you put in new technology that requires training,
[10:02.300 --> 10:05.000]  the staff is not skilled for it, you lost.
[10:05.620 --> 10:07.260]  You didn't do your job as a network designer.
[10:10.860 --> 10:13.900]  Keep everything you've gathered information, keep it there.
[10:14.060 --> 10:16.240]  Because it might be something that's not relevant now,
[10:16.280 --> 10:17.600]  it might become relevant down the road.
[10:18.240 --> 10:20.500]  Or again, make sure you have it available,
[10:20.660 --> 10:21.760]  don't throw it away and assume,
[10:21.820 --> 10:22.240]  oh, this is not relevant.
[10:22.260 --> 10:23.740]  I'm never going to use this piece of information.
[10:24.400 --> 10:26.520]  Make good, you need to have good notes.
[10:26.660 --> 10:30.420]  Taking skills probably will be a good thing to do.
[10:31.900 --> 10:36.140]  And first of all, no preconceived notions and ideas.
[10:36.900 --> 10:39.020]  Because if you do, you're going to have a bias towards
[10:39.020 --> 10:40.680]  a certain solution even before you know
[10:40.680 --> 10:41.420]  what the requirements are.
[10:41.760 --> 10:44.760]  You need to make sure that you leave your head open,
[10:44.820 --> 10:48.040]  a mind open to everything can happen.
[10:48.320 --> 10:51.540]  So if you avoid those preconceived notions, that means,
[10:52.300 --> 10:55.660]  you're open to adjust, so you might have an idea
[10:55.660 --> 10:58.700]  of what you want to do, but then you're much more willing
[10:58.700 --> 11:02.100]  and able to adjust and change course based on what you hear.
[11:02.820 --> 11:05.180]  If you're going to say, it's going to be VXLan no matter what.
[11:06.440 --> 11:08.820]  You end up saying, this is not VXLan, it's not the right fit.
[11:10.800 --> 11:12.940]  Then again, you lost, you didn't do your job.
[11:14.580 --> 11:16.540]  And you don't want to make assumptions,
[11:16.720 --> 11:19.920]  so you want to talk to the people, ask them questions.
[11:20.800 --> 11:21.520]  Never assume.
[11:21.520 --> 11:25.120]  Never assume anything unless you've been told
[11:25.120 --> 11:26.260]  you can assume this.
[11:26.740 --> 11:28.700]  So never automatically assume anything.
[11:30.140 --> 11:32.960]  And finally, the 2 a.m. in the morning test,
[11:33.200 --> 11:35.680]  if somebody calls you, can you justify the decisions
[11:35.680 --> 11:39.080]  you have made, right?
[11:39.840 --> 11:42.860]  Can you at any point say, why did you choose VXLan?
[11:42.980 --> 11:45.340]  Oh, it was because you told me this, this, this,
[11:45.420 --> 11:46.840]  and you have this requirement, this requirement,
[11:47.420 --> 11:49.300]  and you have the skills to support it.
[11:50.160 --> 11:50.600]  Okay.
[11:51.520 --> 11:52.160]  That's the right decision.
[11:52.300 --> 11:54.040]  But if you can't, you're probably wrong.
[11:55.180 --> 11:57.580]  Then, if you can't justify decisions, again,
[11:57.700 --> 11:59.500]  you haven't done your job right.
[12:02.480 --> 12:05.020]  So network designer, you will work with high-level designs.
[12:06.120 --> 12:08.980]  So these are not going to be anything about protocol timers
[12:08.980 --> 12:11.960]  or how you implement OSPF in the areas,
[12:12.120 --> 12:14.600]  or if it's going to be ISIs, what kind of routing
[12:14.600 --> 12:15.180]  protocols you use.
[12:15.380 --> 12:17.520]  You're going to define it's going
[12:17.520 --> 12:19.600]  to be ISIs because of the skill set you have,
[12:19.660 --> 12:21.360]  or you're already using it in the network.
[12:21.900 --> 12:24.920]  But you don't get to typically don't do deal
[12:24.920 --> 12:26.780]  with all the details behind client.
[12:26.900 --> 12:28.500]  That will be part of the low-level design
[12:29.080 --> 12:32.260]  with an implementation engineer, such as an CCAE or CCP,
[12:32.440 --> 12:34.120]  would actually do the actual implementation.
[12:36.340 --> 12:38.540]  And this high-level design, it's just
[12:38.540 --> 12:40.540]  a few of the common things you've put in there.
[12:40.640 --> 12:43.320]  So you will describe all the design that you're proposing.
[12:43.920 --> 12:46.460]  You will gather all the gathered information,
[12:46.460 --> 12:47.820]  say this is what I've been told.
[12:48.300 --> 12:49.940]  So based on this, I've been told.
[12:50.600 --> 12:51.500]  I can meet the requirements.
[12:51.500 --> 12:53.940]  I can meet these requirements by doing like this, and this,
[12:53.940 --> 12:56.180]  and this, and then describe this entire solution
[12:56.180 --> 12:59.080]  from point A to point B. And again,
[12:59.940 --> 13:01.820]  explain why the decisions were made.
[13:02.600 --> 13:04.860]  Because it makes it easy for the customer
[13:04.860 --> 13:08.520]  to understand why you're doing the way you're doing.
[13:08.720 --> 13:10.200]  Because they told you this.
[13:10.400 --> 13:12.020]  You told me this, so I'm going to do this.
[13:12.660 --> 13:13.060]  OK.
[13:13.260 --> 13:16.540]  So they can say, OK, we told you to do so,
[13:16.620 --> 13:17.920]  but actually, we were in mistake.
[13:18.340 --> 13:19.520]  We should not have told you that,
[13:19.520 --> 13:20.640]  because we were going to do this instead.
[13:20.640 --> 13:22.340]  Then it doesn't fall back on you.
[13:22.440 --> 13:24.940]  You can actually say, I made a decision
[13:24.940 --> 13:28.240]  based on what you told me, so let's re-work the case
[13:28.240 --> 13:31.520]  and make sure it actually goes well, and we fix the problem.
[13:34.040 --> 13:35.680]  You might also have to do a little bit of migration
[13:35.680 --> 13:39.460]  planning, figure out who's going to be involved,
[13:39.740 --> 13:40.420]  and things like that.
[13:40.500 --> 13:41.740]  So it might be high-level planning
[13:41.740 --> 13:42.560]  you need to do as well.
[13:43.760 --> 13:45.980]  But typically, again, this is more for the implementation
[13:45.980 --> 13:48.680]  side, but it's going to be, depending
[13:48.680 --> 13:50.380]  on your organization, it might be a little,
[13:50.640 --> 13:52.420]  trade-off, or it might be a little bit more differently
[13:52.420 --> 13:55.120]  cut between implementation and design.
[13:56.040 --> 13:58.560]  You want to start by listing bill of materials, statement
[13:58.560 --> 14:00.400]  of works, and other documents that you do.
[14:01.600 --> 14:03.180]  This is, of course, important to know.
[14:03.300 --> 14:05.500]  Let's say, OK, this is going to be what you have to order.
[14:05.620 --> 14:10.160]  This is the amount of hours you need to invest to actually get
[14:10.160 --> 14:10.520]  this done.
[14:10.900 --> 14:13.040]  But that's going to be part of the high-level design as well.
[14:13.680 --> 14:15.240]  And at the end of the day, this is
[14:15.240 --> 14:16.860]  going to be the document you present to your customer.
[14:17.160 --> 14:20.440]  And they sign off on that and tell, yes, now you've done.
[14:20.440 --> 14:21.060]  Good job.
[14:21.220 --> 14:23.120]  And now we can proceed with the actual implementation.
[14:23.460 --> 14:25.920]  So typically, from high-level design to implementation
[14:25.920 --> 14:28.320]  is done can be several months, maybe even years,
[14:28.940 --> 14:30.360]  depending on the size of the project.
[14:30.680 --> 14:32.000]  But the high-level design is going
[14:32.000 --> 14:33.660]  to be the basis of everything that's
[14:33.660 --> 14:36.500]  going to happen all the way down along that line
[14:36.500 --> 14:39.880]  to make sure that, at the end of the day,
[14:39.940 --> 14:41.840]  you have this implemented in a way that
[14:41.840 --> 14:44.440]  is meaningful to the business that you're working with.
[14:46.140 --> 14:47.440]  So I have a little example here.
[14:47.600 --> 14:49.000]  It's going to be very, very simple.
[14:50.820 --> 14:54.560]  We have a very small data center here for last core distribution,
[14:54.980 --> 14:56.160]  very small customer.
[14:57.420 --> 14:58.860]  So this is what they have today.
[14:59.480 --> 15:01.480]  You get a call from the customer.
[15:02.260 --> 15:03.500]  And they're going to talk a little about,
[15:03.620 --> 15:05.220]  well, we need additional capacity,
[15:05.300 --> 15:07.020]  and we want a second DC side.
[15:07.240 --> 15:08.800]  OK, who doesn't want a second DC side?
[15:08.940 --> 15:09.960]  There's 15 kilometers.
[15:10.160 --> 15:11.620]  Sorry, I'm European, so I'm going to use kilometers.
[15:12.260 --> 15:13.780]  15 kilometers between sites.
[15:13.960 --> 15:15.700]  They will need full layer 2 mobility.
[15:16.340 --> 15:18.640]  They need to VM or containers that
[15:18.640 --> 15:20.420]  can move across both data centers.
[15:20.440 --> 15:22.380]  And they have plenty of fiber options.
[15:22.720 --> 15:23.540]  OK, cool.
[15:25.720 --> 15:27.440]  But it doesn't help you much.
[15:27.620 --> 15:29.940]  You know there's a few very basic requirements.
[15:30.260 --> 15:31.540]  You need a second DC side.
[15:31.700 --> 15:34.200]  But at the end of the day, you can't really work with this.
[15:34.380 --> 15:35.640]  You need more information.
[15:36.520 --> 15:39.800]  But the only thing we can use is that we want a second DC side.
[15:40.020 --> 15:40.560]  All right.
[15:41.760 --> 15:43.980]  OK, we're going to replicate and build a new site.
[15:44.100 --> 15:44.660]  It's complete identical.
[15:46.180 --> 15:48.120]  OK, next step, we have to figure out
[15:48.660 --> 15:50.340]  how to connect these.
[15:50.440 --> 15:50.560]  How do we connect these together?
[15:52.360 --> 15:54.140]  And again, with the information we have,
[15:54.240 --> 15:55.080]  it's not going to be a lot.
[15:55.240 --> 15:57.400]  So this is where technical knowledge comes in.
[15:57.500 --> 15:59.320]  So you might start looking a little bit
[15:59.320 --> 16:02.660]  about all the options that are available that can solve
[16:02.660 --> 16:04.400]  the problem you're trying to do, right?
[16:05.040 --> 16:05.900]  What are you going to do?
[16:05.980 --> 16:07.140]  You're going to use SDN or traditional network.
[16:07.340 --> 16:09.520]  You're going to use BTP, EVPAN, BX LAN.
[16:09.580 --> 16:11.060]  You're going to use some kind of WDM system
[16:11.060 --> 16:12.460]  to connect the sites.
[16:13.700 --> 16:15.660]  And these are just some of the examples.
[16:15.840 --> 16:17.920]  But this is where your technical knowledge comes in.
[16:18.020 --> 16:18.900]  And you figure out.
[16:18.900 --> 16:22.940]  You make a short list of things that might solve the problem
[16:22.940 --> 16:24.660]  you're trying to, you're tasked to solve.
[16:25.500 --> 16:28.460]  At the end of the day, what is the answer?
[16:29.360 --> 16:32.440]  All right, all the information, it depends.
[16:33.180 --> 16:34.800]  Because the context you're putting it in
[16:34.800 --> 16:35.920]  is what really matters.
[16:36.460 --> 16:38.440]  So at this point, you would have to go to the customer
[16:38.440 --> 16:40.400]  and say, thank you for the assignment.
[16:42.260 --> 16:44.240]  But let's sit down and have a cup of coffee.
[16:44.360 --> 16:46.560]  And let's talk a little bit about what you actually need.
[16:47.100 --> 16:48.820]  So we're going to take the first version.
[16:48.820 --> 16:52.720]  Here is that you sit down, have a talk, and say, OK,
[16:52.860 --> 16:53.860]  we don't have a big team.
[16:53.960 --> 16:54.680]  It's a small company.
[16:54.860 --> 16:56.060]  And they're always busy.
[16:56.260 --> 16:57.240]  And they want to try out training.
[16:57.720 --> 16:59.360]  And they want to do things simple.
[16:59.500 --> 17:01.160]  They don't have, because of the skills,
[17:01.380 --> 17:02.700]  they don't have everything ready.
[17:02.860 --> 17:04.700]  So they don't have any automation plans.
[17:04.880 --> 17:05.980]  And something that's standard.
[17:07.420 --> 17:08.460]  They don't have any more.
[17:08.600 --> 17:11.440]  So again, CapEx, capital expenditure.
[17:11.700 --> 17:13.940]  So that means if you buy a piece of equipment,
[17:14.060 --> 17:15.040]  that means it's a CapEx.
[17:15.420 --> 17:17.220]  And OpEx is operational cost.
[17:17.460 --> 17:17.780]  Right?
[17:17.780 --> 17:19.980]  So they don't have any CapEx, so you
[17:19.980 --> 17:22.960]  can't buy additional hardware, except for the new site.
[17:23.180 --> 17:25.400]  But you can't buy anything for the existing site.
[17:25.480 --> 17:27.880]  You can only buy for the new site.
[17:29.840 --> 17:31.520]  So you chew a little bit on that.
[17:31.660 --> 17:32.140]  You come back.
[17:32.220 --> 17:36.260]  And then you're going to look and say, hey, simple.
[17:36.460 --> 17:37.140]  They want something simple.
[17:38.240 --> 17:40.420]  Do a simple layer 2 extension between the sites.
[17:40.620 --> 17:43.480]  Make a port channel to avoid any spanning tree issues.
[17:44.040 --> 17:45.640]  Is it ideal by today's standards?
[17:45.920 --> 17:46.960]  No, probably not.
[17:47.780 --> 17:48.700]  But this is what the customer wants.
[17:49.340 --> 17:51.360]  They want something that's simple and one standard base.
[17:51.420 --> 17:53.940]  OK, you're going to throw in a port channel with LACP
[17:53.940 --> 17:55.560]  to keep track of all the links.
[17:56.100 --> 17:57.620]  And you have the full layer 2 mobility.
[17:57.840 --> 18:00.840]  You're checking off all the boxes with a very simple solution.
[18:01.100 --> 18:03.400]  And they have the fibers available so you
[18:03.400 --> 18:04.380]  can connect them as you want.
[18:05.640 --> 18:07.920]  This meets the requirements of the customer.
[18:09.700 --> 18:11.620]  But it's not modern.
[18:11.960 --> 18:12.940]  It's not fancy.
[18:13.080 --> 18:14.660]  It's not cool by today's standards.
[18:15.220 --> 18:16.060]  But it works.
[18:16.320 --> 18:17.140]  Gets the job done.
[18:17.780 --> 18:18.380]  All right?
[18:19.100 --> 18:20.860]  So let's imagine another situation.
[18:21.100 --> 18:22.440]  You reset here.
[18:22.560 --> 18:23.100]  We go back.
[18:23.200 --> 18:24.200]  And you go over to talk to the customer.
[18:24.320 --> 18:26.960]  And they say, OK, we can add some complexity
[18:26.960 --> 18:28.080]  because we've got skills.
[18:28.160 --> 18:29.560]  We've got good people working for us.
[18:30.660 --> 18:33.540]  We want as much control of the end-to-end path as possible.
[18:33.840 --> 18:34.800]  We've got some cabbage.
[18:34.880 --> 18:36.240]  We can buy some new gear if we need to.
[18:37.080 --> 18:38.140]  We need automation.
[18:38.880 --> 18:41.820]  And we want centralized policy management if we can.
[18:42.040 --> 18:47.640]  So again, preferred versus need, make sure you know those things
[18:47.780 --> 18:51.040]  and say it's a strict requirement or a nice-to-have requirement.
[18:52.240 --> 18:53.120]  There are differences.
[18:53.260 --> 18:54.160]  So it's a preferred.
[18:54.340 --> 18:55.540]  If you can add it, perfect.
[18:55.700 --> 18:57.860]  If you can't, just say it's not possible.
[18:58.680 --> 19:01.620]  But if it's we must have this, then you can't really
[19:02.160 --> 19:03.060]  get away from not doing it.
[19:04.080 --> 19:06.480]  And they need a threefold increase in our need
[19:06.480 --> 19:08.880]  number of links because they know they have done their forecast.
[19:09.060 --> 19:10.220]  So they think in the next 12 months,
[19:10.300 --> 19:11.540]  we need even more capacity.
[19:12.200 --> 19:13.000]  OK, cool.
[19:14.720 --> 19:16.440]  Then let's build a spine-and-leaf architecture.
[19:17.780 --> 19:19.040]  Connect the leaf to each other.
[19:19.140 --> 19:22.820]  You have some WDM system in the middle to do all the links
[19:22.820 --> 19:25.800]  so you can add multiple channels as the capacity needs change.
[19:27.160 --> 19:29.260]  And you can add SDM controllers if you
[19:29.260 --> 19:32.340]  want that automation capability or you
[19:32.340 --> 19:34.340]  want centralized policy management.
[19:34.680 --> 19:35.780]  You can add SDM controllers.
[19:36.220 --> 19:38.220]  You can add Ansible.
[19:38.520 --> 19:39.980]  You can add all those things along the way,
[19:40.080 --> 19:42.180]  again, based on the requirements of the skill set
[19:42.180 --> 19:42.680]  of the customer.
[19:42.940 --> 19:43.860]  You can add this.
[19:44.060 --> 19:47.480]  And this is really two very different
[19:47.480 --> 19:50.020]  ways of solving the same problem here.
[19:50.140 --> 19:52.260]  Because this can offer layer 2 mobility as well.
[19:53.320 --> 19:58.260]  It offers the additional capacity just in a more modern way
[19:58.780 --> 20:00.120]  because these are the requirements
[20:00.120 --> 20:02.180]  that you can meet now and build something that's
[20:02.180 --> 20:04.540]  much more up to them, up to today's standards.
[20:08.520 --> 20:09.380]  There's only one more.
[20:09.420 --> 20:13.100]  You can always find more than one way to do it.
[20:13.780 --> 20:17.380]  The thing is you have to figure out which one is the best one.
[20:18.420 --> 20:19.920]  And what would you recommend?
[20:20.120 --> 20:22.060]  Because, of course, if there are two solutions that
[20:22.060 --> 20:24.640]  would do the exact same thing in the exact same way,
[20:24.800 --> 20:27.580]  make the same requirements, and meet all the same things,
[20:28.700 --> 20:31.760]  then you essentially have to choose and say, OK,
[20:31.860 --> 20:32.720]  I would recommend this.
[20:32.860 --> 20:35.500]  Because then it's your personal, might be a personal experience,
[20:35.560 --> 20:37.600]  say, this works better in this environment than this.
[20:38.500 --> 20:42.100]  But then, again, you would have to document it and say,
[20:42.220 --> 20:45.420]  because of personal experience, we recommend this way.
[20:45.520 --> 20:47.360]  Because it works better for you.
[20:47.380 --> 20:48.720]  It works better traditionally in these kinds of environments.
[20:50.200 --> 20:52.420]  I mentioned before, must prefer, require,
[20:52.560 --> 20:53.540]  expect, not have, need to have.
[20:54.120 --> 20:57.580]  Make sure you do it because this is a change in the requirements
[20:57.580 --> 20:58.080]  that you have.
[20:58.980 --> 21:01.660]  And do you need to meet them, or should you need them,
[21:01.720 --> 21:02.660]  or can you meet them?
[21:02.860 --> 21:04.980]  It all makes sure you do it.
[21:05.620 --> 21:07.480]  Now, again, go back, ask.
[21:08.140 --> 21:10.480]  One single person probably won't have all your answers,
[21:10.680 --> 21:12.400]  so you'll have to talk to a bunch of people.
[21:13.080 --> 21:16.560]  Again, network engineers, CFOs, CTOs,
[21:18.000 --> 21:20.180]  maybe even users, because if they're complaining
[21:20.180 --> 21:23.440]  about issues when they connect to the application,
[21:23.780 --> 21:25.120]  there might be, you need to implement some kind
[21:25.120 --> 21:27.020]  of quality of service you need to add on top of it.
[21:27.720 --> 21:29.900]  So talk to all the stakeholders that's there.
[21:30.020 --> 21:31.880]  Make sure you get all the input, because otherwise,
[21:32.380 --> 21:33.940]  you're only going to get one side of the affair.
[21:34.080 --> 21:36.740]  If you only talk to the CFO, you're going to be tasked
[21:36.740 --> 21:39.600]  with something that's cheap, doesn't cost a lot of money,
[21:39.960 --> 21:42.540]  but it doesn't meet what the technical requirements are.
[21:42.840 --> 21:44.280]  And if you only talk to the network engineers,
[21:44.380 --> 21:45.860]  they're going to say, we want the latest and greatest
[21:45.860 --> 21:46.540]  and coolest features.
[21:46.540 --> 21:46.540]  That's not going to work.
[21:46.540 --> 21:46.540]  That's not going to work.
[21:46.560 --> 21:49.880]  But the CFO is going to say, no, we're not going to pay
[21:49.880 --> 21:50.160]  for that.
[21:50.620 --> 21:53.020]  So as the network designer, you are the bridge
[21:53.020 --> 21:57.460]  between the business and the technology side.
[21:57.740 --> 22:00.040]  You can speak both languages, or you should be able
[22:00.040 --> 22:00.920]  to speak both languages.
[22:02.220 --> 22:05.160]  That's what the true network design does if you work
[22:05.160 --> 22:06.440]  with this in a professional way.
[22:06.620 --> 22:07.980]  You can speak to both sides.
[22:10.880 --> 22:13.460]  Make sure that you spend the time you need.
[22:14.160 --> 22:15.940]  Don't say, oh, I'm going to scroll.
[22:15.940 --> 22:17.560]  I don't have more time today, so I'm not going
[22:17.560 --> 22:18.300]  to ask more questions.
[22:18.540 --> 22:20.800]  I think the rest of your information I didn't get
[22:20.800 --> 22:22.520]  my answers to, I'm just going to assume things.
[22:22.740 --> 22:24.580]  No. Spend the time.
[22:25.020 --> 22:27.860]  Spend all the time you need to make sure you get all
[22:27.860 --> 22:29.780]  the information you need to build the design
[22:29.780 --> 22:31.440]  in the way you're expected to.
[22:32.920 --> 22:34.820]  Again, I've said this many times, but don't forget,
[22:35.200 --> 22:37.220]  there's going to be expectations from the business side,
[22:37.300 --> 22:38.180]  and there's going to be requirements
[22:38.180 --> 22:41.520]  from the business side, not only the technical side.
[22:41.700 --> 22:44.840]  So again, money wins at the end of the day.
[22:44.880 --> 22:45.640]  It is king.
[22:49.820 --> 22:51.860]  So when you talk about it in context with CCDE,
[22:52.000 --> 22:54.840]  because I would be a fool not to talk about the CCDE
[22:54.840 --> 22:58.200]  when I'm here, this is exactly what we do with the CCDE.
[22:58.260 --> 22:59.120]  We test you on these skills.
[23:00.300 --> 23:04.380]  We test you on the ability to speak to both the technical
[23:04.380 --> 23:07.940]  side and the business side, gathering all information,
[23:08.300 --> 23:09.700]  analyzing what you're working with.
[23:09.840 --> 23:11.120]  That's what we test you on.
[23:11.880 --> 23:13.420]  That's going to be something that you have to do
[23:13.420 --> 23:13.880]  business-wise.
[23:15.800 --> 23:17.280]  Why are you doing this?
[23:17.420 --> 23:22.000]  It's because you want to be more agile in your future changes,
[23:22.120 --> 23:24.540]  in your strategic direction in your company,
[23:24.780 --> 23:25.780]  whatever it might be.
[23:26.120 --> 23:27.500]  But this is what we test you on.
[23:27.700 --> 23:31.280]  This is all, we will test you and give you anything
[23:31.280 --> 23:36.620]  that you need, and ultimately you will build a solution
[23:37.240 --> 23:39.220]  that matches this at the end of the day.
[23:39.900 --> 23:42.840]  And we do this in an eight-hour marathon
[23:43.620 --> 23:44.200]  as you take the exam.
[23:44.680 --> 23:46.920]  I hope to see you to take the exam one day, of course,
[23:47.040 --> 23:49.440]  so feel free to ask, and reach out if you do that.
[23:50.100 --> 23:53.340]  But it's going to be four of these scenarios.
[23:53.780 --> 23:56.380]  And then every scenario is going to be like I just talked about.
[23:56.480 --> 23:57.920]  It's going to be you have a bunch of requirements.
[23:58.200 --> 23:59.540]  You have an existing topology.
[24:00.180 --> 24:02.900]  What can we do to make XYZ happen?
[24:03.340 --> 24:04.440]  This is what we do.
[24:04.580 --> 24:06.500]  And you do that for four different scenarios.
[24:07.260 --> 24:09.360]  And these are not connected in any way.
[24:10.000 --> 24:13.880]  So when you finish with the two-hour, you have to clear your mind, reset
[24:13.880 --> 24:14.180]  your mind.
[24:14.180 --> 24:17.440]  And go back and start the next scenario.
[24:17.620 --> 24:18.760]  And it's going to be completely different.
[24:18.880 --> 24:19.980]  It's going to be different requirements.
[24:20.220 --> 24:21.200]  It's going to be a different company.
[24:21.480 --> 24:23.460]  It might even be a completely different vertical
[24:23.460 --> 24:24.140]  you're working with.
[24:25.000 --> 24:28.800]  But for the DE, this is going to be across more verticals.
[24:28.800 --> 24:30.560]  It can be enterprise, of course.
[24:30.680 --> 24:31.760]  This is what we focus on.
[24:32.440 --> 24:33.860]  But it can be wireless.
[24:34.140 --> 24:35.800]  It can be even collaboration.
[24:36.340 --> 24:37.240]  It can be routing switching.
[24:37.440 --> 24:37.980]  It can be WAN.
[24:38.300 --> 24:40.760]  It can be anything that you would find within an enterprise.
[24:42.660 --> 24:44.000]  Then we have this little thing here.
[24:44.000 --> 24:46.680]  At the end, we call the area of expertise, which
[24:46.680 --> 24:49.100]  is a more specialized scenario.
[24:49.340 --> 24:52.380]  Again, same concepts apply, but just focusing
[24:52.380 --> 24:56.600]  on something a little more could be service provider oriented.
[24:56.720 --> 24:58.020]  So if you work as a service provider,
[24:58.120 --> 25:00.600]  it might be more relevant for you to take this scenario.
[25:00.740 --> 25:03.540]  We have something that deals with data centers and cloud.
[25:04.020 --> 25:06.220]  And we have one that works heavily on wireless.
[25:06.420 --> 25:10.200]  So radio planning, all that stuff that goes with site
[25:10.200 --> 25:12.900]  surveys, all the stuff that goes with a problem wireless
[25:12.900 --> 25:13.300]  assignment.
[25:13.300 --> 25:13.300]  That's fine.
[25:14.300 --> 25:17.340]  But at the end of the day, it's an eight-hour scenario-based
[25:17.340 --> 25:17.800]  exam.
[25:19.660 --> 25:21.020]  And it is a marathon.
[25:21.540 --> 25:23.800]  But I tell you, I can guarantee you, this is worth it.
[25:26.240 --> 25:29.300]  Because I know from talking to those who pass the exam,
[25:29.560 --> 25:32.280]  whenever they take the CCDE and they get the CCDE badge,
[25:32.900 --> 25:36.400]  the door is open to talk to CXO-level people.
[25:36.620 --> 25:40.140]  You can now get talking time in front of CTOs, CFOs.
[25:40.180 --> 25:43.280]  Because the industry knows the CCDE is able to sort out the data.
[25:43.280 --> 25:43.280]  It's not just a matter of time.
[25:43.280 --> 25:45.060]  We can speak business and technology.
[25:45.180 --> 25:46.740]  It's not focused on technology alone.
[25:47.580 --> 25:48.480]  We can speak both.
[25:48.840 --> 25:52.260]  We are the gap between business and technology.
[25:54.580 --> 25:55.860]  Whenever you do one of these exams,
[25:57.000 --> 25:59.340]  it's going to have a lot of introductions.
[25:59.680 --> 26:02.280]  So it's going to tell you what the company are, what they do,
[26:02.480 --> 26:04.180]  what are their strategies, all that stuff
[26:04.180 --> 26:07.060]  that you would need to be able to get a glimpse and get
[26:07.060 --> 26:08.160]  an idea of what you're working with,
[26:08.340 --> 26:10.340]  get a company background, topology joins.
[26:10.680 --> 26:12.340]  And then you will get some ongoing correspondence.
[26:12.340 --> 26:13.340]  You will get emails.
[26:13.780 --> 26:17.780]  So again, imagine you're sitting in a meeting with your customer
[26:17.780 --> 26:20.180]  and they tell you, this is what we want.
[26:20.600 --> 26:22.800]  Oh, by the way, and then you get another email saying,
[26:22.940 --> 26:23.700]  oh, we also want this.
[26:24.060 --> 26:25.500]  This is no longer relevant.
[26:26.700 --> 26:27.500]  This is what you get.
[26:28.240 --> 26:31.660]  This is presented to you along the full two-hour scenario.
[26:32.980 --> 26:34.920]  And you have to figure out, it is your job
[26:34.920 --> 26:36.480]  to figure out what the relevant information is
[26:36.480 --> 26:40.120]  and make the decisions with the questions you get in your exam.
[26:41.420 --> 26:42.260]  And first of all,
[26:42.340 --> 26:43.760]  do not fight the test.
[26:44.620 --> 26:47.340]  Because if you think, oh, I know better than this.
[26:47.460 --> 26:48.700]  This is much better.
[26:48.740 --> 26:50.220]  I know exactly how this should work.
[26:50.980 --> 26:52.700]  You're not listening to what we're
[26:52.700 --> 26:54.120]  saying in all the documentation.
[26:55.640 --> 26:58.080]  Because again, leave your outside knowledge
[26:58.080 --> 26:59.700]  and preconceived notions at the door.
[27:00.480 --> 27:02.660]  You're in a bubble for two hours or eight hours.
[27:02.920 --> 27:03.740]  You live in that.
[27:04.560 --> 27:06.980]  So don't fight the test by saying, I know better.
[27:07.460 --> 27:09.120]  This is a sure way to fail the exam.
[27:09.340 --> 27:10.700]  I can guarantee you that.
[27:13.480 --> 27:17.320]  And when you do this, you become a different network
[27:17.320 --> 27:18.200]  engineer than you are today.
[27:18.400 --> 27:21.380]  If you add this business skill set
[27:21.380 --> 27:22.940]  on top of your technical skill set,
[27:23.860 --> 27:25.440]  it's going to be a completely different game.
[27:25.740 --> 27:28.240]  Because you can get different kind of roles.
[27:28.620 --> 27:32.460]  You can get talk time in front of CFOs, CTOs.
[27:33.020 --> 27:34.360]  It's going to change your career.
[27:34.860 --> 27:37.560]  Of course, if you're genuinely interested in working
[27:37.560 --> 27:41.820]  with networks, if you're 100% network implementation, then this
[27:41.820 --> 27:42.800]  probably is not for you.
[27:43.560 --> 27:46.620]  But if you need that design, and you love network design,
[27:46.780 --> 27:49.540]  and you want to do more network design, have a look at the DE.
[27:50.500 --> 27:52.260]  Because you'll learn that there's more to it
[27:52.260 --> 27:54.800]  than just the business side or the technology side.
[27:54.880 --> 27:57.520]  There's a ton of business side you need to meet, too.
[28:00.260 --> 28:02.360]  So that's pretty much what I wanted to say here.
[28:03.840 --> 28:05.760]  I'll be around if you want to ask questions.
[28:05.920 --> 28:07.260]  Feel free to stop by.
[28:07.380 --> 28:09.120]  I'm typically around the certification lounge here.
[28:10.780 --> 28:11.800]  And we have tons of data.
[28:11.800 --> 28:13.380]  We have lots of different training that you can do.
[28:14.480 --> 28:16.720]  So feel free to come by, ask us questions.
[28:16.880 --> 28:19.460]  Ask some of my colleagues in the certification lounge
[28:19.460 --> 28:22.980]  about learning paths and Cisco U, how they
[28:22.980 --> 28:24.760]  can help you on your journey.
[28:25.100 --> 28:27.180]  So feel free to come by and say that.
[28:27.460 --> 28:30.160]  And with that said, thank you for stopping by.
[28:30.320 --> 28:31.040]  Appreciate your time.
[28:41.800 --> 28:42.140]  And I'll see you next time.
(utube_transcriber_env) PS C:\Users\kiman\Documents\GitHub\CCDE_Cisco> 
(utube_transcriber_env) PS C:\Users\kiman\Documents\GitHub\CCDE_Cisco> 