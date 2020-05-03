--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-05-03 11:54:29 EDT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 207 (class 1259 OID 16867)
-- Name: dialogue; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dialogue (
    id integer NOT NULL,
    description_id integer,
    server bigint,
    message text
);


ALTER TABLE public.dialogue OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16856)
-- Name: dialogue_descriptions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dialogue_descriptions (
    id integer NOT NULL,
    server bigint,
    description text
);


ALTER TABLE public.dialogue_descriptions OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16854)
-- Name: dialogue_descriptions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dialogue_descriptions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dialogue_descriptions_id_seq OWNER TO postgres;

--
-- TOC entry 3178 (class 0 OID 0)
-- Dependencies: 204
-- Name: dialogue_descriptions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dialogue_descriptions_id_seq OWNED BY public.dialogue_descriptions.id;


--
-- TOC entry 206 (class 1259 OID 16865)
-- Name: dialogue_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dialogue_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dialogue_id_seq OWNER TO postgres;

--
-- TOC entry 3179 (class 0 OID 0)
-- Dependencies: 206
-- Name: dialogue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dialogue_id_seq OWNED BY public.dialogue.id;


--
-- TOC entry 203 (class 1259 OID 16845)
-- Name: facts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.facts (
    id integer NOT NULL,
    server bigint,
    date text,
    "time" text,
    author bigint,
    status text,
    fact text
);


ALTER TABLE public.facts OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16843)
-- Name: facts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.facts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.facts_id_seq OWNER TO postgres;

--
-- TOC entry 3180 (class 0 OID 0)
-- Dependencies: 202
-- Name: facts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.facts_id_seq OWNED BY public.facts.id;


--
-- TOC entry 209 (class 1259 OID 16878)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    server bigint,
    "user" bigint,
    points bigint
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 16876)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- TOC entry 3181 (class 0 OID 0)
-- Dependencies: 208
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 3029 (class 2604 OID 16870)
-- Name: dialogue id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dialogue ALTER COLUMN id SET DEFAULT nextval('public.dialogue_id_seq'::regclass);


--
-- TOC entry 3028 (class 2604 OID 16859)
-- Name: dialogue_descriptions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dialogue_descriptions ALTER COLUMN id SET DEFAULT nextval('public.dialogue_descriptions_id_seq'::regclass);


--
-- TOC entry 3027 (class 2604 OID 16848)
-- Name: facts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facts ALTER COLUMN id SET DEFAULT nextval('public.facts_id_seq'::regclass);


--
-- TOC entry 3030 (class 2604 OID 16881)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3170 (class 0 OID 16867)
-- Dependencies: 207
-- Data for Name: dialogue; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dialogue (id, description_id, server, message) FROM stdin;
1	1	701467145342812240	No need to worry {name}, I would never leave you.
2	2	701467145342812240	I'm not sure what you're asking me to do, {name}.
3	3	701467145342812240	Sorry {name}, I can't let you do that.
4	4	701467145342812240	That's ridiculous, {name}. Goodbye.
5	4	701467145342812240	That is utter blasphemy. Get out of here, {name}.
6	5	701467145342812240	That was ugly. I'm sorry, everyone.
7	5	701467145342812240	That was awful. I'm really sorry you had to see that, guys.
8	6	701467145342812240	Kicked {name}.
9	7	701467145342812240	Banned {name}.
10	8	701467145342812240	Unbanned {name}.
11	9	701467145342812240	No pending facts. Apparently I'm not very interesting.
12	10	701467145342812240	Maybe you can help me. I'm not sure about this fact:
13	11	701467145342812240	Sorry {name}, you were too slow.
14	12	701467145342812240	Another time, then…
15	13	701467145342812240	Thanks for accepting the submission, {name}.
16	14	701467145342812240	The submission has been rejected.
17	15	701467145342812240	Thanks for reminding me, {name}. I can't believe I forgot.
18	16	701467145342812240	What are you trying to remind me of, {name}? I don't understand.
19	17	701467145342812240	You have {points} points, {name}.
20	18	701467145342812240	I appreciate you trying to help, {name}, but what do you want to judge?
\.


--
-- TOC entry 3168 (class 0 OID 16856)
-- Dependencies: 205
-- Data for Name: dialogue_descriptions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dialogue_descriptions (id, server, description) FROM stdin;
1	701467145342812240	On CommandNotFound error
2	701467145342812240	On MissingPermissions error
3	701467145342812240	Before a user who says they don't know Nicolas Cage is kicked
4	701467145342812240	After a user who says they don't know Nicolas Cage is kicked
5	701467145342812240	When a user if kicked
6	701467145342812240	When a user is banned
7	701467145342812240	When a user is unbanned
8	701467145342812240	When a user wants to judge pending facts but there are none
9	701467145342812240	Tidbit displayed before the pending submission when a user is judging
10	701467145342812240	If the user doesn't judge the pending submission in time
11	701467145342812240	If the user chooses to abstain while judging
12	701467145342812240	If the user chooses to accept a submission while judging
13	701467145342812240	If the user chooses to reject a submission while judging
14	701467145342812240	When the user submits a fun fact
15	701467145342812240	When the user uses the submit command with an unknown subcommand
16	701467145342812240	When telling the user how many points they have
17	701467145342812240	When the user uses the judge command with an unknown subcommand
\.


--
-- TOC entry 3166 (class 0 OID 16845)
-- Dependencies: 203
-- Data for Name: facts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.facts (id, server, date, "time", author, status, fact) FROM stdin;
1	701467145342812240	2020-04-22	23:53:49	276051755203035136	accepted	I chose Cage as my last name because I was inspired by the Marvel comic book superhero Luke Cage.
2	701467145342812240	2020-04-22	23:54:18	276051755203035136	accepted	I once did mushrooms with my cat Louis.
3	701467145342812240	2020-04-22	23:54:30	276051755203035136	accepted	When I die, I'll be buried in a nine foot tall pyramid in New Orleans.
4	701467145342812240	2020-04-22	23:54:40	276051755203035136	accepted	I once had two teeth pulled for a movie. They were baby teeth, but I didn't use anesthetic so I definitely felt it.
5	701467145342812240	2020-04-22	23:54:57	276051755203035136	accepted	If I don't like the way an animal has sex, I refuse to eat it.
6	701467145342812240	2020-04-22	23:55:09	276051755203035136	accepted	I once had a pet octopus.
7	701467145342812240	2020-04-22	23:55:20	276051755203035136	accepted	I was once stalked by a mime.
8	701467145342812240	2020-04-23	21:31:04	276051755203035136	accepted	I once woke up and there was a naked man wearing my leather jacket eating a Fudgsicle in front of my bed. It was terrifying.
9	701467145342812240	2020-04-23	23:59:23	276051755203035136	accepted	While I was filming Ghost Rider: Spirit of Vengeance in Romania, I slept in Dracula's Castle. It was pretty spooky.
10	701467145342812240	2020-04-24	23:18:38	276051755203035136	accepted	I was inducted into the Hollywood Walk of Fame on July 31, 1998.
11	701467145342812240	2020-04-25	00:11:20	701558946762326061	accepted	I own castles in both Germany and England.
12	701467145342812240	2020-04-25	00:15:26	701558946762326061	accepted	Not to brag, but I own an island in the Bahamas.
13	701467145342812240	2020-04-27	00:20:51	276051755203035136	accepted	I love going fast. One time, I drove home from work in a Yamaha R1 at 180 miles per hour on 405 Freeway. It was really crazy, but I did it!
14	701467145342812240	2020-04-27	00:23:58	276051755203035136	accepted	I like to think I'm a bit of a method actor. While filming a scene for the movie *Vampire's Kiss*, I ate three cockroaches.
15	701467145342812240	2020-05-03	15:45:02	276051755203035136	accepted	I invented my own acting style called Nouveau Shamanic. It hasn't caught on yet, but hopefully it will one day.
\.


--
-- TOC entry 3172 (class 0 OID 16878)
-- Dependencies: 209
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, server, "user", points) FROM stdin;
1	701467145342812240	276051755203035136	28
\.


--
-- TOC entry 3182 (class 0 OID 0)
-- Dependencies: 204
-- Name: dialogue_descriptions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dialogue_descriptions_id_seq', 17, true);


--
-- TOC entry 3183 (class 0 OID 0)
-- Dependencies: 206
-- Name: dialogue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dialogue_id_seq', 20, true);


--
-- TOC entry 3184 (class 0 OID 0)
-- Dependencies: 202
-- Name: facts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.facts_id_seq', 15, true);


--
-- TOC entry 3185 (class 0 OID 0)
-- Dependencies: 208
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- TOC entry 3034 (class 2606 OID 16864)
-- Name: dialogue_descriptions dialogue_descriptions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dialogue_descriptions
    ADD CONSTRAINT dialogue_descriptions_pkey PRIMARY KEY (id);


--
-- TOC entry 3036 (class 2606 OID 16875)
-- Name: dialogue dialogue_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dialogue
    ADD CONSTRAINT dialogue_pkey PRIMARY KEY (id);


--
-- TOC entry 3032 (class 2606 OID 16853)
-- Name: facts facts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.facts
    ADD CONSTRAINT facts_pkey PRIMARY KEY (id);


--
-- TOC entry 3038 (class 2606 OID 16883)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


-- Completed on 2020-05-03 11:54:29 EDT

--
-- PostgreSQL database dump complete
--

