"""
Version and Changelog for Traktor DJ NowPlaying Discord Bot

This file contains the current version and complete changelog. And 5 most recent versions are detailed.
For the latest version information, check this file or the GUI application.
"""

__version__ = "1.1.5"
__version_info__ = (1, 1, 5)

# =============================================================================
# VERSIONING SCHEME
# =============================================================================
# We follow Semantic Versioning (SemVer) vA.B.C:
# - A (Major): Major rewrites, breaking changes, architectural overhauls
# - B (Minor): New features, enhancements, backwards-compatible additions  
# - C (Patch): Bug fixes, maintenance updates, minor improvements

# =============================================================================
# COMPLETE CHANGELOG (Newest First) - Only the most recent 5 versions detailed
# =============================================================================

# -----------------------------------------------------------------------------
# Version 1.1.5 - PATCH RELEASE (2025-06-16)
# -----------------------------------------------------------------------------
# Commited missing files
#
# BUG FIXES:
# - Commited missing files
#

# -----------------------------------------------------------------------------
# Version 1.1.4 - PATCH RELEASE (2025-06-16)
# -----------------------------------------------------------------------------
# Fixed Build issue with filename
#
# BUG FIXES:
# - Fixed Build issue with filename
#
# TECHNICAL DETAILS:
# - Broken array in build.py fixed

# -----------------------------------------------------------------------------
# Version 1.1.3 - PATCH RELEASE (2025-06-16)
# -----------------------------------------------------------------------------
# GUI layout improvements and startup messaging consistency
#
# BUG FIXES:
# - Fixed GUI layout issues with controls panel being cut off or having excessive whitespace
# - Improved button width calculation to prevent text truncation
# - Fixed controls frame sizing to ensure proper display of all elements
#
# IMPROVEMENTS:
# - Enhanced GUI layout with better proportional sizing between controls and log panels
# - Improved startup messaging consistency to match refresh operation details
# - Optimized button sizing algorithm for better text accommodation
# - Added minimum width constraints to prevent UI cramping
#
# TECHNICAL DETAILS:
# - Refactored controls frame grid configuration for better layout management
# - Improved column weight distribution between control and log panels
# - Enhanced button width calculation with better emoji and text handling
# - Streamlined GUI initialization process

# -----------------------------------------------------------------------------
# Version 1.1.2 - PATCH RELEASE (2025-06-16)
# -----------------------------------------------------------------------------
# GUI cleanup and layout optimization
#
# BUG FIXES:
# - Fixed button panel layout to prevent any visual cutoff issues
# - Cleaned up unused button references and methods
#
# IMPROVEMENTS:
# - Optimized GUI layout for better visual appearance
# - Streamlined control panel with only essential buttons
# - Maintained consistent button sizing and spacing
# - Improved code organization by removing test artifacts
#
# TECHNICAL DETAILS:
# - Updated button_texts array to reflect actual buttons
# - Improved code organization and layout optimization

# -----------------------------------------------------------------------------
# Version 1.1.1 - PATCH RELEASE (2025-06-16)
# -----------------------------------------------------------------------------
# Critical Discord message limit fixes and search optimization
#
# BUG FIXES:
# - Fixed Discord 2000-character message limit causing search timeouts
# - Fixed incorrect result count displays in truncation messages
# - Corrected message formatting (truncation info now on separate line)
#
# PERFORMANCE IMPROVEMENTS:
# - Removed artificial MAX_SONGS limit - now dynamically fits maximum results
# - Implemented smart message truncation with precise character counting
# - Two-pass algorithm for optimal result fitting within Discord limits
# - Dynamic message length calculation for both truncated and non-truncated scenarios
#
# ENHANCEMENTS:
# - Improved user feedback with accurate "showing X of Y results" messages
# - Enhanced collection display with smart truncation for new songs feature
# - Better debug logging for message length monitoring
# - Consistent 2000-character limit handling across all Discord responses
#
# TECHNICAL DETAILS:
# - Dynamic string length calculation instead of fixed buffers
# - Precise character counting for message components
# - Optimal result fitting algorithm maximizes displayed songs
# - Proper line formatting for professional Discord message appearance

# =============================================================================
# Earlier Versions (0.1 - 1.1.0) 
# =============================================================================
# - 1.1.0: Major performance optimization and architectural enhancement
# - 1.0.3: PATCH RELEASE (2025-06-15) Complete rebranding and naming consistency
# - 1.0.2: Documentation streamlining and build improvements - README reduced by 50%+, static executable naming
# - 1.0.1: Bug fixes and command cleanup - Fixed Discord command count, cleaned up commands, GUI-only admin functions
# - 1.0.0: Complete rewrite - Modular GUI application with cogs system and distribution
# - 0.13: Code quality improvements with enhanced null safety and type annotations
# - 0.12: Dynamic Traktor version detection with enhanced path management
# - 0.11: Live streaming notifications with role mentions and community features
# - 0.10: Complete song request management with full CRUD operations
# - 0.9: Interactive song request system - Major code reorganization, timeout handling
# - 0.8: NowPlaying integration and history management
# - 0.7: Enhanced search algorithm and code organization  
# - 0.6: Major robustness improvements and debugging capabilities
# - 0.5: Enhanced text formatting and improved user feedback
# - 0.4: Configurable new songs tracking with date filtering
# - 0.3: New songs discovery and enhanced collection management
# - 0.2: Core functionality improvements
# - 0.1: Basic search functionality
