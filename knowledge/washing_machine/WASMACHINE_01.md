# WASMACHINE_01 — Lossless audit uit ChatGPT-chat

Originele chatnaam: huidige ChatGPT-vraag rond Wasmachine HA / washok-statuslamp / was-advies / debugprotocol / logging.

## Scope

Dit bestand bewaart kennis uit deze chat over de Home Assistant wasmachine-flow. Buiten scope: vorstwaarschuwing buitenkranen, behalve als voorbeeld van foutieve vermenging.

## Harde afbakening

Wasmachine en vorstwaarschuwing mogen niet door elkaar lopen. In deze chat is expliciet gecorrigeerd dat vorstwaarschuwing buitenkranen niets met het wasmachineverhaal te maken heeft.

## Werkflow-afspraken van gebruiker

- Helpers, templates, input_* en timers worden via configuration.yaml gedaan.
- Pad helpers/config: Settings → Add-ons → File Editor → Open Web UI → configuration.yaml.
- De gebruiker plakt volledige configuration.yaml; ChatGPT past minimaal aan en geeft volledige file terug.
- Automations worden via Automation Editor → YAML gedaan, tenzij expliciet automations.yaml wordt gebruikt.
- DevTools Actions is alleen voor test/service-call, niet voor volledige automation.
- DevTools Templates is alleen voor verificatie-output.
- Bij lossless blokken altijd monospace/copyable.
- Geen vage instructies: altijd exact waar plakken, exacte YAML/template, verwacht resultaat en wat terug te plakken.

## Bevestigde entities

Wasmachine:
- sensor.huis_washok_wasmachine_vermogen
- sensor.huis_washok_wasmachine_stroom
- sensor.huis_washok_wasmachine_spanning

Presence:
- input_boolean.presence_mark

Notify:
- notify.mobile_app_iphone_mark

Statuslamp:
- light.huis_washok_statuslamp

Regen / weer genoemd maar niet volledig bewezen:
- binary_sensor.huis_washok_regensensor
- sensor.huis_washok_regen_forecast

Buitenlampen genoemd maar niet bewezen via entity-export:
- light.washok_buiten_1
- light.washok_buiten_2
- light.washok_buiten_3
- light.washok_buiten_4

Knoppen:
- Knop A = was uit machine.
- Knop B = was hangt buiten en impliceert A.
- Exacte entity_id/device_id/endpoint/cluster van Knop A/B zijn in deze chat NIET bewezen.

## Helpers in configuration.yaml

input_boolean:
- input_boolean.wasmachine_pending — was ligt nog in machine / actie nodig.
- input_boolean.wasmachine_has_run — cyclus gezien.
- input_boolean.wasmachine_halfhour_sent — halfuur reminder verzonden.
- input_boolean.wasmachine_18_sent — 18:00 reminder verzonden.
- input_boolean.wasmachine_20_sent — 20:00 reminder verzonden.

input_datetime:
- input_datetime.wasmachine_done_at — klaar-tijd.
- input_datetime.wasmachine_halfhour_due_at — halfuur reminder-tijd.
- input_datetime.wasmachine_mark_last_arrived — Mark laatst aangekomen.
- input_datetime.wasmachine_mark_last_notified — Mark laatst gemeld.

Niet bewezen / later genoemd / open:
- wash_task_active
- waslijn_active
- stop_lock
- rain_confirmed
- cooldown helpers
- wasmachine-specifieke timers

## Wasmachine-detectie

Start:
- sensor.huis_washok_wasmachine_vermogen > 10 W gedurende 2 minuten.
- Zet has_run ON.
- Zet pending OFF.
- Reset halfhour_sent, 18_sent, 20_sent OFF.

Klaar:
- sensor.huis_washok_wasmachine_vermogen < 3 W gedurende 5 minuten.
- Alleen geldig als has_run ON was.
- Zet pending ON.
- Zet done_at = now.
- Berekent halfhour_due_at.
- Zet has_run OFF.

Definitie heeft gedraaid:
- >10 W minimaal 2 minuten.

Definitie klaar:
- <3 W minimaal 5 minuten na een gezien run-event.

## Notificaties / reminders

Direct bij klaar:
- Bericht: 🧺 Was is klaar.
- Alleen als Mark thuis is of binnen 2 minuten na aankomst.
- Dedupe moet OK zijn.

Reminder “was ligt nog in de machine”:
- Halverwege tussen done_at en 18:00, afgerond op :00/:30.
- 18:00 reminder.
- 20:00 reminder.
- Bij thuiskomen van Mark.

Dedupe:
- Minimaal 55 minuten tussen meldingen voor Mark.
- Helper: input_datetime.wasmachine_mark_last_notified.

Presence:
- mark_home_or_2min = presence_mark ON of now - mark_last_arrived <= 2 minuten.

Halverwege-afronding:
- minuten <15 → :00.
- minuten <45 → :30.
- minuten >=45 → volgende volle uur.

Quiet-hours genoemd maar niet bewezen in huidige automation:
- 22:30–10:00 ma–za.
- zondag vóór 11:59 geen push, behalve na knop A/B.

## Cutoff / silent logic

In v1.0.1 automation:
- cutoff_ts = min(done_at + 13 uur, 20:45 op done-dag).
- should_be_silent = now > cutoff_ts.
- Na cutoff: pending OFF, halfhour_sent OFF, 18_sent OFF, 20_sent OFF, has_run OFF.

Conflicten:
- Later tekstueel is ook “10 uur cutoff” genoemd voor rood alarm.
- Een vraag noemde “max 14u guard”.
- Definitieve cutoff voor geïntegreerde lamp/outdoor-flow is daarom nog open.

## Huidige automation uit chat

Alias:
- Wasmachine — was klaar reminders (Mark) v1.0.1

Mode:
- single

Triggers:
- vermogen >10W 2min.
- vermogen <3W 5min.
- presence_mark to on.
- time_pattern elke minuut.
- time 18:00.
- time 20:00.

Belangrijke variabelen:
- now_ts
- done_ts
- done_date
- t18_ts
- t20_ts
- cutoff_2045_ts
- cutoff_ts
- last_notified_ts
- last_arrived_ts
- dedupe_ok
- mark_home_or_2min
- pending_on
- has_run_on
- half_sent
- sent18
- sent20
- before_20
- within_13h
- should_be_silent
- due_ts

Branches:
- cutoff cleanup.
- start detected.
- Mark arrived.
- done detected.
- 18:00 reminder.
- 20:00 reminder.
- half-way reminder.

Belangrijke bug/ontdekking:
- Tijdens testen stond de automation disabled; daardoor kwamen geen meldingen. Na enable moest live gedrag opnieuw bekeken worden.

## Statuslamp / lampadvies

Statuslamp is leidend; telefoonmeldingen zijn toelichting.

Knipperen = aandacht.

Knop A:
- was uit machine.
- reset pending/reminders/has_run.
- lamp uit/neutraal.

Knop B:
- was hangt buiten.
- impliceert A.
- reset pending automatisch.
- start buiten-sessie / adviesmodus.

Lamplogica volgens correctie:
- Wasmachine draait → lamp UIT.
- Was klaar / pending normaal → WIT knipper.
- Kleur+WIT knipper alleen bij buiten-sessie.
- Groen/wit knipper = veilig.
- Oranje/wit knipper = twijfel.
- Rood/wit knipper = schadegevaar of regen NU.
- Regen NU bevestigd → altijd rood/wit override.
- Cutoff → rood alarmknipper, stopt alleen via knop.

Onbekend:
- exacte effectnamen/statuslamp capabilities.
- exacte buitenlamp capabilities.

## Was buiten / weerlogica

Gedeeltelijk besproken, niet volledig geïmplementeerd in deze chat.

Besproken:
- regen NU via binary_sensor.huis_washok_regensensor.
- regen forecast / rain soon via sensor.huis_washok_regen_forecast, ≤90 min genoemd.
- outdoor_advice met mogelijke waarden SAFE / MAYBE / DANGER.
- Regen NU override naar rood/wit.

Niet besproken / onbekend:
- KNMI/Buienradar/webbronnen concreet.
- puntensysteem of wegingen.
- windkracht/droogtijd/wasgewicht-combinatie-effecten.
- dry_ok en stop_in_min bron.

## Loggingwens / event-log

Doel: logging toevoegen zodat ha_get_history en event-log kinderziektes kunnen opsporen.

Te loggen kritieke events:
1. SESSION_DONE.
2. pending ON.
3. outdoor_advice wijziging.
4. regen_confirmed wijziging.
5. notification_sent.
6. notification_blocked.
7. button_pressed.
8. too_late ON.
9. lamp kleurwissel.
10. session_closed.

Lamp log events:
- UIT → WIT KNIPPER.
- WIT → GROEN/WIT.
- WIT → ORANJE/WIT.
- elke status → ROOD/WIT bij regen NU.
- elke status → ROOD ALARM bij cutoff.
- elke status → UIT bij knop/reset/nieuwe sessie.

Notification types:
- WAS_KLAAR.
- WAS_LIGT_NOG_IN_MACHINE_HALF.
- WAS_LIGT_NOG_IN_MACHINE_18.
- WAS_LIGT_NOG_IN_MACHINE_20.
- WAS_LIGT_NOG_IN_MACHINE_THUISKOMST.

Blocked reasons:
- dedupe.
- quiet_hours.
- too_late.
- pending_off.
- not_home.

Button logs:
- Knop A: pending_before/after, lamp_before/after.
- Knop B: pending_before/after, outside_session_started, lamp_before/after, outdoor_advice.
- B impliceert A moet in logging zichtbaar zijn.

## Debug logger automation

Er is een debug logger automation voorgesteld:
- Alias: Wasmachine — debug logger (Mark) v1.0.0.
- Trigger op relevante wasmachine helpers/datetimes/presence.
- Action: persistent_notification.create met snapshot.

Status:
- Voorgesteld maar niet bevestigd geïnstalleerd.

## DevTools Actions protocol — bewezen lessons

Bewezen werkend in huidige HA UI:
- DevTools → Actions accepteerde service-call-only YAML zoals:
  service: input_boolean.turn_on
  target:
    entity_id: input_boolean.wasmachine_pending

Ook notify service-call-only werkte met groen vinkje.

Niet mengen:
- Geen automation YAML in Actions.
- Geen Jinja/template in Actions.
- Geen Actions YAML in Templates.
- Geen meerdere YAML-documenten.

Verificatie:
- Groen vinkje is nuttig, maar state/template-output is leidend.

Conflict:
- Sommige protocolvarianten zeiden dat Actions top-level action: nodig had. User bewees later dat service-call-only werkte. Voor deze chat: service-call-only is de bewezen vorm voor DevTools Actions.

## Debugprotocol / communicatieprotocol lessons

Bij elke uitvoerbare stap moet ChatGPT leveren:
- WAAR plakken.
- Exacte YAML of template.
- Verwacht succes-signaal.
- Wat gebruiker terugplakt.

Geen stap zonder code.
Geen “plak result” zonder te geven waarmee result geproduceerd wordt.
Niet opnieuw vragen naar bekende workflow.
Lossless = monospace/copyable.

## Laatste bekende state snapshot

Na template-check:
- now_local: 2026-01-07 00:33:08+01:00.
- pending: false.
- has_run: false.
- half_sent: false.
- sent18: false.
- sent20: false.
- done_at: 2026-01-05 16:26:34.
- halfhour_due_at: 2026-01-05 17:00:00.
- mark_last_arrived: 2026-01-06 00:03:30.
- mark_last_notified: 2026-01-06 00:59:00.
- dedupe_ok_now: true.
- mark_home_or_2min: true.
- should_be_silent: true.

Interpretatie:
- veilige stille toestand.
- geen actieve pending.
- cutoff bereikt.

## Openstaande punten

- Exacte Knop A entity_id/device_id/endpoint/cluster.
- Exacte Knop B entity_id/device_id/endpoint/cluster.
- Definitieve cutoff: 10h vs 13h/20:45 vs max 14h.
- Bestaat sensor.huis_washok_regen_forecast en welk datatype/attribute?
- Exacte statuslamp effects/capabilities.
- Exacte buitenlamp capabilities.
- Moeten extra helpers waslijn_active/wash_task_active/stop_lock/rain_confirmed worden aangemaakt?
- Is debug logger automation geïnstalleerd?
- Is intelligent message automation elders al uitgewerkt?

## Audit rondes

Auditrondes uitgevoerd in deze sessie: 5.

Kennisblokken toegevoegd:
1. Scope en afbakening.
2. Entities.
3. Helpers.
4. Detectie.
5. Reminders.
6. Cutoff.
7. Automation-structuur.
8. Statuslamp.
9. Was buiten / weerlogica.
10. Logging.
11. DevTools Actions protocol.
12. Openstaande conflicten.
