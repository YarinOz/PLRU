THIS_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
FUNC_DIR := ../func1

##################
# Build directory
##################
OBJDIR  = obj
CFLAGS += -I./$(OBJDIR) 
CFLAGS += -I$(FUNC_DIR)/$(OBJDIR)
CFLAGS += -Wall -Wno-unused-variable
####################
# Files and folders
####################
SRCS_EXE = 	ifndef.c

OBJS_MAIN	= 	$(addprefix $(OBJDIR)/,$(patsubst %.c,%.o,$(SRCS_EXE)))
OBJS_FUNC	= 	$(addprefix $(FUNC_DIR)/$(OBJDIR)/,$(notdir $(patsubst %.c,%.o,$(shell find $(FUNC_DIR)/*.c))))
##########
# Targets
##########
all: clean func1 exe
# Compiling targets

exe: $(OBJS_MAIN) $(OBJS_FUNC)
	$(CC) -o $@ $^ $(LDFLAGS) -lrt -lm

func1:
	$(MAKE) -C $(FUNC_DIR) 

$(OBJDIR)/%.o: %.c | objdir
	$(CC) $(CFLAGS) -c $< -o $@

objdir:
	@mkdir -p $(OBJDIR) 

run: 
	@./exe

clean: 
	@rm -rf $(OBJDIR) exe
# all:clean ifndef

# ifndef: ifndef.c 
# 	gcc -o exe ifndef.c

# run: 
# 	@./exe

# clean:
# 	rm -rf exe