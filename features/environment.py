# import logging
# import allure
# from logs import logs_config

# def before_all(context):
#     context.log = logs_config.get_logs()
#     context.log.info("Test execution started")

# def before_scenario(context, scenario):
#     context.log.info(f"Starting scenario: {scenario.name}")

# def after_scenario(context, scenario):
#     if scenario.status == "failed":
#         context.log.error(f"Scenario '{scenario.name}' failed")
#         allure.dynamic.title(f"Failed: {scenario.name}")
#         allure.dynamic.description(scenario.description or "No description provided")
#         allure.attach(context.log.handlers[0].baseFilename, name="Log File", attachment_type=allure.attachment_type.TEXT)
#     else:
#         context.log.info(f"Scenario '{scenario.name}' passed")
#         allure.dynamic.title(f"Passed: {scenario.name}")
#         allure.dynamic.description(scenario.description or "No description provided")
#         allure.attach(context.log.handlers[0].baseFilename, name="Log File", attachment_type=allure.attachment_type.TEXT)

# def after_all(context):
#     context.log.info("Test execution finished")
